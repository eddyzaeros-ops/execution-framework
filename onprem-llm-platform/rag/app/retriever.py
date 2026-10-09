"""混合檢索：向量 + BM25，兩路都先做權限過濾，再以 RRF 合併，選配 rerank。"""
import json
import os

from qdrant_client import QdrantClient
from qdrant_client.models import FieldCondition, Filter, MatchAny, Range
from rank_bm25 import BM25Okapi

from . import config, llm
from .auth import User
from .chunking import tokenize


def acl_filter(user: User) -> Filter:
    return Filter(must=[
        FieldCondition(key="level", range=Range(lte=user.level)),
        FieldCondition(key="project", match=MatchAny(any=sorted(user.projects))),
    ])


class Retriever:
    def __init__(self):
        self.client = QdrantClient(url=config.QDRANT_URL)
        self.reload()

    def reload(self) -> None:
        path = os.path.join(config.INDEX_DIR, "chunks.jsonl")
        self.chunks: list[dict] = []
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                self.chunks = [json.loads(line) for line in f if line.strip()]
        self.bm25 = BM25Okapi([tokenize(f"{c['title']} {c['section']} {c['text']}")
                               for c in self.chunks]) if self.chunks else None

    def _vector(self, query: str, user: User) -> list[dict]:
        vec = llm.embed([query])[0]
        hits = self.client.search(config.COLLECTION, query_vector=vec,
                                  query_filter=acl_filter(user), limit=config.TOP_K_VECTOR)
        return [h.payload for h in hits]

    def _bm25(self, query: str, user: User) -> list[dict]:
        if not self.bm25:
            return []
        scores = self.bm25.get_scores(tokenize(query))
        order = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        out = []
        for i in order:
            if scores[i] <= 0 or len(out) >= config.TOP_K_BM25:
                break
            if user.can_read(self.chunks[i]):
                out.append(self.chunks[i])
        return out

    def search(self, query: str, user: User, k: int = config.TOP_K_FINAL) -> list[dict]:
        ranked: dict[str, float] = {}
        by_id: dict[str, dict] = {}
        for results in (self._vector(query, user), self._bm25(query, user)):
            for rank, c in enumerate(results):
                ranked[c["chunk_id"]] = ranked.get(c["chunk_id"], 0.0) + 1.0 / (60 + rank)
                by_id[c["chunk_id"]] = c
        cands = [by_id[i] for i in sorted(ranked, key=ranked.get, reverse=True)][: k * 3]

        scores = llm.rerank(query, [c["text"] for c in cands])
        if scores:
            cands = [c for _, c in sorted(zip(scores, cands), key=lambda x: x[0], reverse=True)]
        # 防禦性檢查：即使上游出錯，也不回傳無權限段落
        return [c for c in cands if user.can_read(c)][:k]
