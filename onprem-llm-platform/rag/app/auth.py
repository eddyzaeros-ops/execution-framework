"""身分與權限：API Key -> 使用者（密等、可存取專案）。

MVP 用檔案對應；正式環境請改接 LDAP / AD / SSO。
"""
from dataclasses import dataclass, field
import hashlib
import hmac
import yaml
from fastapi import Header, HTTPException

from . import config


@dataclass(frozen=True)
class User:
    name: str
    level: int
    projects: frozenset = field(default_factory=frozenset)

    def can_read(self, chunk: dict) -> bool:
        return chunk["level"] <= self.level and chunk["project"] in self.projects


def _hash(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()


def load_users(path: str = config.USERS_FILE) -> dict[str, User]:
    """users.yaml 中只存 API Key 的 SHA256，不存明文。"""
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    users = {}
    for u in data.get("users", []):
        users[u["api_key_sha256"]] = User(u["name"], int(u["level"]), frozenset(u.get("projects", [])))
    return users


_USERS: dict[str, User] | None = None


def get_users() -> dict[str, User]:
    global _USERS
    if _USERS is None:
        _USERS = load_users()
    return _USERS


def current_user(x_api_key: str = Header(...)) -> User:
    h = _hash(x_api_key)
    for stored, user in get_users().items():
        if hmac.compare_digest(stored, h):
            return user
    raise HTTPException(status_code=401, detail="invalid api key")
