"""設定：全部由環境變數讀取。"""
import os

LLM_URL = os.getenv("LLM_URL", "http://localhost:8000/v1")
LLM_MODEL = os.getenv("LLM_SERVED_NAME", "domain-llm")
EMBED_URL = os.getenv("EMBED_URL", "http://localhost:8001/v1")
EMBED_MODEL = os.getenv("EMBED_SERVED_NAME", "domain-embed")
RERANK_URL = os.getenv("RERANK_URL", "")  # 空字串表示不啟用
RERANK_MODEL = os.getenv("RERANK_SERVED_NAME", "domain-rerank")
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
COLLECTION = os.getenv("COLLECTION", "docs")

USERS_FILE = os.getenv("USERS_FILE", "config/users.yaml")
INDEX_DIR = os.getenv("INDEX_DIR", "data/index")
AUDIT_FILE = os.getenv("AUDIT_FILE", "data/audit/audit.jsonl")
CORPUS_DIR = os.getenv("CORPUS_DIR", "corpus")

TOP_K_VECTOR = int(os.getenv("TOP_K_VECTOR", "20"))
TOP_K_BM25 = int(os.getenv("TOP_K_BM25", "20"))
TOP_K_FINAL = int(os.getenv("TOP_K_FINAL", "6"))
CHUNK_CHARS = int(os.getenv("CHUNK_CHARS", "800"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "120"))
TIMEOUT = float(os.getenv("HTTP_TIMEOUT", "120"))
