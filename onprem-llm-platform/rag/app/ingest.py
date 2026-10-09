"""文件匯入：語料目錄 -> 切分 -> embedding -> Qdrant + BM25 段落檔。

每份 .md / .txt 文件需有同名的 .meta.yaml，例如 spec.md.meta.yaml：
    doc_id: SPEC-001
    title: 電源子系統規格書
    version: B
    level: 2        # 密等數字，越大越高
    project: PRJ-A

用法：python -m app.ingest [語料目錄]
"""
import json
import os
import sys
import uuid
from pathlib import Path

import yaml
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PayloadSchemaType, PointStruct, VectorParams

from . import config, llm
from .chunking import split_markdown

REQUIRED = ("doc_id", "title", "version", "level", "project")


def load_corpus(root: str) -> list[dict]:
    chunks = []
    for path in sorted(Path(root).rglob("*")):
        if path.suffix.lower() not in (".md", ".txt"):
            continue
        meta_path = path.with_name(path.name + ".meta.yaml")
        if not meta_path.exists():
            print(f"[略過] 缺少 metadata：{path}")
            continue
        meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
        missing = [k for k in REQUIRED if k not in meta]
        if missing:
            print(f"[略過] {meta_path} 缺少欄位 {missing}")
            continue
        text = path.read_text(encoding="utf-8")
        for i, c in enumerate(split_markdown(text)):
            chunk_id = f"{meta['doc_id']}#{i:04d}"
            chunks.append({
                "chunk_id": chunk_id,
                "doc_id": meta["doc_id"],
                "title": meta["title"],
                "version": str(meta["version"]),
                "level": int(meta["level"]),
                "project": meta["project"],
                "section": c["section"],
                "text": c["text"],
            })
    return chunks


def main(root: str) -> None:
    chunks = load_corpus(root)
    if not chunks:
        print("沒有可匯入的段落")
        return
    print(f"共 {len(chunks)} 段，計算 embedding 中…")
    vectors = llm.embed([f"{c['title']} {c['section']}\n{c['text']}" for c in chunks])

    client = QdrantClient(url=config.QDRANT_URL)
    client.recreate_collection(
        config.COLLECTION,
        vectors_config=VectorParams(size=len(vectors[0]), distance=Distance.COSINE),
    )
    client.create_payload_index(config.COLLECTION, "level", PayloadSchemaType.INTEGER)
    client.create_payload_index(config.COLLECTION, "project", PayloadSchemaType.KEYWORD)
    points = [
        PointStruct(id=str(uuid.uuid5(uuid.NAMESPACE_URL, c["chunk_id"])), vector=v, payload=c)
        for c, v in zip(chunks, vectors)
    ]
    for i in range(0, len(points), 256):
        client.upsert(config.COLLECTION, points[i:i + 256])

    os.makedirs(config.INDEX_DIR, exist_ok=True)
    with open(os.path.join(config.INDEX_DIR, "chunks.jsonl"), "w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    print("匯入完成")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else config.CORPUS_DIR)
