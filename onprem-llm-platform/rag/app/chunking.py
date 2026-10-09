"""文件切分與斷詞。

- 依 Markdown 標題切段，保留章節路徑。
- 過長段落再依字數切分（含重疊）。
- 斷詞：英數字詞 + 中文字元 bigram，不需外部斷詞字典。
"""
import re

from . import config

_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
_TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9\-_.]*|[\u4e00-\u9fff]")


def tokenize(text: str) -> list[str]:
    out: list[str] = []
    prev = None
    for tok in _TOKEN.findall(text.lower()):
        if len(tok) == 1 and "\u4e00" <= tok <= "\u9fff":
            out.append(tok)
            if prev:
                out.append(prev + tok)
            prev = tok
        else:
            out.append(tok)
            prev = None
    return out


def _split_long(text: str, size: int, overlap: int) -> list[str]:
    if len(text) <= size:
        return [text]
    parts, start = [], 0
    while start < len(text):
        parts.append(text[start:start + size])
        if start + size >= len(text):
            break
        start += size - overlap
    return parts


def split_markdown(text: str, size: int = config.CHUNK_CHARS,
                   overlap: int = config.CHUNK_OVERLAP) -> list[dict]:
    """回傳 [{section, text}]，section 為章節路徑。"""
    sections: list[tuple[str, str]] = []
    path: list[str] = []
    buf: list[str] = []

    def flush():
        body = "\n".join(buf).strip()
        if body:
            sections.append((" > ".join(path) or "(前言)", body))

    for line in text.splitlines():
        m = _HEADING.match(line)
        if m:
            flush()
            buf = []
            level = len(m.group(1))
            path[:] = path[: level - 1] + [m.group(2).strip()]
        else:
            buf.append(line)
    flush()

    chunks = []
    for section, body in sections:
        for piece in _split_long(body, size, overlap):
            chunks.append({"section": section, "text": piece})
    return chunks
