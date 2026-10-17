"""LRU-K Cache eviction policy implementation."""

import time
from collections import deque
from typing import Any, Dict


class LRUKCache:
    """LRU-K cache eviction policy tracking K-th backward reference distance."""

    def __init__(self, capacity: int, k: int = 2):
        if capacity <= 0 or k <= 0:
            raise ValueError("Capacity and k must be positive integers.")
        self.capacity = capacity
        self.k = k
        self.data: Dict[Any, Any] = {}
        self.history: Dict[Any, deque] = {}

    def get(self, key: Any, default: Any = None) -> Any:
        """Retrieve key value and record reference timestamp."""
        if key not in self.data:
            return default
        self._record_access(key)
        return self.data[key]

    def put(self, key: Any, value: Any) -> None:
        """Insert or update key-value pair."""
        if key in self.data:
            self.data[key] = value
            self._record_access(key)
            return

        if len(self.data) >= self.capacity:
            self._evict()

        self.data[key] = value
        self._record_access(key)

    def _record_access(self, key: Any) -> None:
        if key not in self.history:
            self.history[key] = deque(maxlen=self.k)
        self.history[key].append(time.time())

    def _evict(self) -> None:
        """Evict key with the oldest k-th reference, or oldest recent reference."""
        victim = None
        oldest_k_time = float("inf")

        for key in self.data:
            hist = self.history.get(key, deque())
            if len(hist) < self.k:
                k_time = 0.0
            else:
                k_time = hist[0]

            if k_time < oldest_k_time:
                oldest_k_time = k_time
                victim = key

        if victim is not None:
            del self.data[victim]
            if victim in self.history:
                del self.history[victim]

    def delete(self, key: Any) -> bool:
        """Remove key from cache."""
        if key in self.data:
            del self.data[key]
            if key in self.history:
                del self.history[key]
            return True
        return False

    def clear(self) -> None:
        """Clear cache contents."""
        self.data.clear()
        self.history.clear()

    def __len__(self) -> int:
        return len(self.data)
