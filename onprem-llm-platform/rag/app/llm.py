"""呼叫 vLLM（OpenAI 相容）的 embedding、rerank、chat。"""
import httpx

from . import config


def embed(texts: list[str], batch: int = 32) -> list[list[float]]:
    vecs: list[list[float]] = []
    with httpx.Client(timeout=config.TIMEOUT) as c:
        for i in range(0, len(texts), batch):
            r = c.post(f"{config.EMBED_URL}/embeddings",
                       json={"model": config.EMBED_MODEL, "input": texts[i:i + batch]})
            r.raise_for_status()
            data = sorted(r.json()["data"], key=lambda d: d["index"])
            vecs.extend(d["embedding"] for d in data)
    return vecs


def rerank(query: str, docs: list[str]) -> list[float] | None:
    """回傳每份文件的分數；未設定 RERANK_URL 或失敗時回傳 None。"""
    if not config.RERANK_URL or not docs:
        return None
    try:
        with httpx.Client(timeout=config.TIMEOUT) as c:
            r = c.post(f"{config.RERANK_URL}/v1/rerank",
                       json={"model": config.RERANK_MODEL, "query": query, "documents": docs})
            r.raise_for_status()
            scores = [0.0] * len(docs)
            for item in r.json()["results"]:
                scores[item["index"]] = item["relevance_score"]
            return scores
    except httpx.HTTPError:
        return None


def chat(messages: list[dict], temperature: float = 0.1, max_tokens: int = 1024) -> str:
    with httpx.Client(timeout=config.TIMEOUT) as c:
        r = c.post(f"{config.LLM_URL}/chat/completions",
                   json={"model": config.LLM_MODEL, "messages": messages,
                         "temperature": temperature, "max_tokens": max_tokens})
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
