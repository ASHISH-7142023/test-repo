"""In-memory caching utilities with TTL expiration and LRU eviction."""

import time
import threading
from collections import OrderedDict
from typing import Any, Optional, Dict, Tuple


class TTLCache:
    """Thread-safe in-memory cache with time-to-live (TTL) expiration per item."""

    def __init__(self, default_ttl_seconds: float = 60.0):
        self.default_ttl = default_ttl_seconds
        self._store: Dict[str, Tuple[Any, float]] = {}
        self._lock = threading.Lock()

    def set(self, key: str, value: Any, ttl: Optional[float] = None) -> None:
        """Store key-value pair with optional custom TTL in seconds."""
        expire_at = time.time() + (ttl if ttl is not None else self.default_ttl)
        with self._lock:
            self._store[key] = (value, expire_at)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve key value if unexpired, else return default."""
        with self._lock:
            if key not in self._store:
                return default
            val, expire_at = self._store[key]
            if time.time() > expire_at:
                del self._store[key]
                return default
            return val

    def delete(self, key: str) -> bool:
        """Delete key from cache."""
        with self._lock:
            if key in self._store:
                del self._store[key]
                return True
            return False

    def clear(self) -> None:
        """Clear all keys in cache."""
        with self._lock:
            self._store.clear()

    def size(self) -> int:
        """Return count of active, non-expired keys."""
        now = time.time()
        with self._lock:
            # Purge expired
            expired_keys = [k for k, (_, exp) in self._store.items() if now > exp]
            for k in expired_keys:
                del self._store[k]
            return len(self._store)


class LRUCache:
    """Thread-safe in-memory Least Recently Used (LRU) cache."""

    def __init__(self, maxsize: int = 128):
        if maxsize <= 0:
            raise ValueError("maxsize must be greater than zero.")
        self.maxsize = maxsize
        self._store: OrderedDict[str, Any] = OrderedDict()
        self._lock = threading.Lock()

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve key and mark as most recently used."""
        with self._lock:
            if key not in self._store:
                return default
            self._store.move_to_end(key)
            return self._store[key]

    def set(self, key: str, value: Any) -> None:
        """Store key-value pair, evicting oldest item if exceeding capacity."""
        with self._lock:
            if key in self._store:
                self._store.move_to_end(key)
            self._store[key] = value
            if len(self._store) > self.maxsize:
                self._store.popitem(last=False)

    def delete(self, key: str) -> bool:
        """Delete key from cache."""
        with self._lock:
            if key in self._store:
                del self._store[key]
                return True
            return False

    def clear(self) -> None:
        """Clear cache."""
        with self._lock:
            self._store.clear()

    def __len__(self) -> int:
        with self._lock:
            return len(self._store)
