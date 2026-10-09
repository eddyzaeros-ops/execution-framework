"""稽核紀錄：只附加寫入 JSONL。"""
import json
import os
import threading
import time

from . import config

_lock = threading.Lock()


def write(event: dict) -> None:
    event = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), **event}
    os.makedirs(os.path.dirname(config.AUDIT_FILE) or ".", exist_ok=True)
    line = json.dumps(event, ensure_ascii=False)
    with _lock, open(config.AUDIT_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")
