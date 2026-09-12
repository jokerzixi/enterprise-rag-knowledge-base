from __future__ import annotations

import json
import sqlite3
import threading
import uuid
from pathlib import Path
from typing import Dict, List, Optional, Protocol

from utils.env_utils import REDIS_URL, SESSION_BACKEND, SESSION_TTL_SECONDS
from utils.log_utils import log

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SQLITE_PATH = ROOT / "datas" / "sessions.db"


class _Store(Protocol):
    def ensure_session(self, session_id: Optional[str] = None) -> str: ...
    def get_messages(self, session_id: str) -> List[dict]: ...
    def add_turn(self, session_id: str, question: str, answer: str) -> None: ...
    def clear(self, session_id: str) -> None: ...


class MemoryStore:
    """进程内回退（无 Redis / SQLite 时）。"""

    def __init__(self, max_turns: int = 8):
        self.max_turns = max_turns
        self._store: Dict[str, List[dict]] = {}
        self._lock = threading.Lock()

    def ensure_session(self, session_id: Optional[str] = None) -> str:
        sid = (session_id or "").strip() or str(uuid.uuid4())
        with self._lock:
            self._store.setdefault(sid, [])
        return sid

    def get_messages(self, session_id: str) -> List[dict]:
        with self._lock:
            return list(self._store.get(session_id, []))

    def add_turn(self, session_id: str, question: str, answer: str) -> None:
        with self._lock:
            turns = self._store.setdefault(session_id, [])
            turns.append({"role": "user", "content": question})
            turns.append({"role": "assistant", "content": answer})
            max_msgs = self.max_turns * 2
            if len(turns) > max_msgs:
                self._store[session_id] = turns[-max_msgs:]

    def clear(self, session_id: str) -> None:
        with self._lock:
            self._store[session_id] = []


class SqliteStore:
    """本地 SQLite 持久化（无需额外服务）。"""

    def __init__(self, db_path: Path, max_turns: int = 8):
        self.max_turns = max_turns
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(str(self.db_path), check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._lock:
            conn = self._connect()
            try:
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS sessions (
                        session_id TEXT PRIMARY KEY,
                        messages_json TEXT NOT NULL DEFAULT '[]',
                        updated_at REAL NOT NULL
                    )
                    """
                )
                conn.commit()
            finally:
                conn.close()

    def ensure_session(self, session_id: Optional[str] = None) -> str:
        import time

        sid = (session_id or "").strip() or str(uuid.uuid4())
        with self._lock:
            conn = self._connect()
            try:
                row = conn.execute(
                    "SELECT session_id FROM sessions WHERE session_id = ?", (sid,)
                ).fetchone()
                if not row:
                    conn.execute(
                        "INSERT INTO sessions(session_id, messages_json, updated_at) VALUES (?, ?, ?)",
                        (sid, "[]", time.time()),
                    )
                    conn.commit()
            finally:
                conn.close()
        return sid

    def get_messages(self, session_id: str) -> List[dict]:
        with self._lock:
            conn = self._connect()
            try:
                row = conn.execute(
                    "SELECT messages_json FROM sessions WHERE session_id = ?",
                    (session_id,),
                ).fetchone()
                if not row:
                    return []
                data = json.loads(row["messages_json"] or "[]")
                return data if isinstance(data, list) else []
            finally:
                conn.close()

    def add_turn(self, session_id: str, question: str, answer: str) -> None:
        import time

        with self._lock:
            conn = self._connect()
            try:
                row = conn.execute(
                    "SELECT messages_json FROM sessions WHERE session_id = ?",
                    (session_id,),
                ).fetchone()
                turns: List[dict] = []
                if row:
                    turns = json.loads(row["messages_json"] or "[]")
                    if not isinstance(turns, list):
                        turns = []
                turns.append({"role": "user", "content": question})
                turns.append({"role": "assistant", "content": answer})
                max_msgs = self.max_turns * 2
                if len(turns) > max_msgs:
                    turns = turns[-max_msgs:]
                conn.execute(
                    """
                    INSERT INTO sessions(session_id, messages_json, updated_at)
                    VALUES (?, ?, ?)
                    ON CONFLICT(session_id) DO UPDATE SET
                        messages_json = excluded.messages_json,
                        updated_at = excluded.updated_at
                    """,
                    (session_id, json.dumps(turns, ensure_ascii=False), time.time()),
                )
                conn.commit()
            finally:
                conn.close()

    def clear(self, session_id: str) -> None:
        import time

        with self._lock:
            conn = self._connect()
            try:
                conn.execute(
                    """
                    INSERT INTO sessions(session_id, messages_json, updated_at)
                    VALUES (?, '[]', ?)
                    ON CONFLICT(session_id) DO UPDATE SET
                        messages_json = '[]',
                        updated_at = excluded.updated_at
                    """,
                    (session_id, time.time()),
                )
                conn.commit()
            finally:
                conn.close()


class RedisStore:
    """Redis 持久化（多 worker / 多实例共享）。"""

    def __init__(self, redis_url: str, max_turns: int = 8, ttl_seconds: int = 604800):
        import redis

        self.max_turns = max_turns
        self.ttl = max(60, int(ttl_seconds))
        # protocol=2：兼容不支持 RESP3 HELLO 的旧版 Redis
        self._r = redis.Redis.from_url(
            redis_url,
            decode_responses=True,
            protocol=2,
        )
        self._r.ping()
        self._prefix = "rag:session:"

    def _key(self, session_id: str) -> str:
        return f"{self._prefix}{session_id}"

    def ensure_session(self, session_id: Optional[str] = None) -> str:
        sid = (session_id or "").strip() or str(uuid.uuid4())
        key = self._key(sid)
        if not self._r.exists(key):
            self._r.set(key, "[]", ex=self.ttl)
        else:
            self._r.expire(key, self.ttl)
        return sid

    def get_messages(self, session_id: str) -> List[dict]:
        raw = self._r.get(self._key(session_id))
        if not raw:
            return []
        data = json.loads(raw)
        return data if isinstance(data, list) else []

    def add_turn(self, session_id: str, question: str, answer: str) -> None:
        key = self._key(session_id)
        turns = self.get_messages(session_id)
        turns.append({"role": "user", "content": question})
        turns.append({"role": "assistant", "content": answer})
        max_msgs = self.max_turns * 2
        if len(turns) > max_msgs:
            turns = turns[-max_msgs:]
        self._r.set(key, json.dumps(turns, ensure_ascii=False), ex=self.ttl)

    def clear(self, session_id: str) -> None:
        self._r.set(self._key(session_id), "[]", ex=self.ttl)


class ConversationMemory:
    """会话记忆门面：优先 Redis，其次 SQLite，最后内存。"""

    def __init__(self, max_turns: int = 8):
        self.max_turns = max_turns
        self.backend_name = "memory"
        self._store: _Store = self._build_store()

    def _build_store(self) -> _Store:
        backend = (SESSION_BACKEND or "auto").strip().lower()

        if backend in ("redis", "auto") and REDIS_URL:
            try:
                store = RedisStore(
                    REDIS_URL,
                    max_turns=self.max_turns,
                    ttl_seconds=SESSION_TTL_SECONDS,
                )
                self.backend_name = "redis"
                log.info(f"会话记忆后端: Redis ({REDIS_URL})")
                return store
            except Exception as exc:
                log.warning(f"Redis 会话不可用，将降级: {exc}")
                if backend == "redis":
                    raise

        if backend in ("sqlite", "auto", "redis"):
            try:
                store = SqliteStore(DEFAULT_SQLITE_PATH, max_turns=self.max_turns)
                self.backend_name = "sqlite"
                log.info(f"会话记忆后端: SQLite ({DEFAULT_SQLITE_PATH})")
                return store
            except Exception as exc:
                log.warning(f"SQLite 会话不可用，将降级到内存: {exc}")
                if backend == "sqlite":
                    raise

        self.backend_name = "memory"
        log.warning("会话记忆后端: 进程内存（重启会丢失）")
        return MemoryStore(max_turns=self.max_turns)

    def ensure_session(self, session_id: Optional[str] = None) -> str:
        return self._store.ensure_session(session_id)

    def get_messages(self, session_id: str) -> List[dict]:
        return self._store.get_messages(session_id)

    def add_turn(self, session_id: str, question: str, answer: str) -> None:
        self._store.add_turn(session_id, question, answer)

    def clear(self, session_id: str) -> None:
        self._store.clear(session_id)

    def format_history(self, session_id: str, max_chars: int = 4000) -> str:
        messages = self.get_messages(session_id)
        if not messages:
            return ""
        lines = []
        for msg in messages:
            role = "用户" if msg.get("role") == "user" else "助手"
            lines.append(f"{role}：{msg.get('content', '')}")
        text = "\n".join(lines)
        if len(text) > max_chars:
            text = text[-max_chars:]
        return text


memory_store = ConversationMemory(max_turns=8)
