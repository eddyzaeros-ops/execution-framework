"""產生 API Key 的 SHA256。用法：python tools/hash_key.py <key>；不帶參數則隨機產生一組。"""
import hashlib
import secrets
import sys

key = sys.argv[1] if len(sys.argv) > 1 else secrets.token_urlsafe(32)
print("key    :", key)
print("sha256 :", hashlib.sha256(key.encode()).hexdigest())
