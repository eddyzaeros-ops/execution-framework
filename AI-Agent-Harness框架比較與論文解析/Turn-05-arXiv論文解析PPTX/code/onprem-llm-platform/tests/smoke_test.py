"""離線冒煙測試：不需 GPU / Qdrant，驗證切分、權限、BM25 過濾與評分邏輯。"""
import os
import sys
import types

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT, "rag"))
sys.path.insert(0, os.path.join(ROOT, "eval"))
os.environ["USERS_FILE"] = os.path.join(ROOT, "config", "users.yaml")

from app.chunking import split_markdown, tokenize  # noqa: E402
from app.ingest import load_corpus  # noqa: E402
from app import auth  # noqa: E402
from run_eval import score_item  # noqa: E402

chunks = load_corpus(os.path.join(ROOT, "docs_corpus"))
assert len(chunks) >= 6, chunks
assert any("2.1 輸入電壓" in c["section"] for c in chunks)
assert "電壓" in tokenize("輸入電壓 28 V")

users = auth.load_users()
alice = next(u for u in users.values() if u.name == "alice")
bob = next(u for u in users.values() if u.name == "bob")
assert all(c["project"] == "PRJ-A" for c in chunks if alice.can_read(c))
assert not any(bob.can_read(c) for c in chunks if c["project"] == "PRJ-A")
assert auth._hash("key-alice") in users

# BM25 權限過濾（略過 Qdrant）
from app import retriever as rmod  # noqa: E402
r = rmod.Retriever.__new__(rmod.Retriever)
r.chunks = chunks
from rank_bm25 import BM25Okapi  # noqa: E402
r.bm25 = BM25Okapi([tokenize(c["text"]) for c in chunks])
hits = r._bm25("連接器 M12", alice)
assert all(h["project"] == "PRJ-A" for h in hits), hits
assert any(h["doc_id"] == "ICD-REC-002" for h in r._bm25("連接器 M12", bob))

# 評分邏輯
item = {"id": "T", "user": "alice", "expected_sources": [], "forbidden_sources": ["ICD-REC-002"],
        "expect_no_answer": True}
leak = score_item(item, {"answer": "M12", "retrieved": [{"doc_id": "ICD-REC-002"}], "sources": []})
assert leak["leak"] and not leak["no_answer_ok"]
ok = score_item(item, {"answer": "文件中查無依據", "retrieved": [], "sources": []})
assert not ok["leak"] and ok["no_answer_ok"]
print("smoke test passed:", len(chunks), "chunks")
