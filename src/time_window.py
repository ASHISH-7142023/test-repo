"""Rolling sliding and tumbling window metric aggregators."""

import time
from collections import deque
from typing import Deque, Tuple, Dict, Optional


class SlidingWindowCounter:
    """Thread-safe time-based sliding window event counter."""

    def __init__(self, window_seconds: float):
        if window_seconds <= 0:
            raise ValueError("Window size must be greater than zero.")
        self.window_seconds = window_seconds
        self._events: Deque[Tuple[float, int]] = deque()

    def record(self, count: int = 1, timestamp: Optional[float] = None) -> None:
        """Record event occurrence at timestamp."""
        ts = timestamp if timestamp is not None else time.time()
        self._events.append((ts, count))

    def _evict_expired(self, now: float) -> None:
        cutoff = now - self.window_seconds
        while self._events and self._events[0][0] < cutoff:
            self._events.popleft()

    def get_count(self, now: Optional[float] = None) -> int:
        """Get total events within the sliding window."""
        ts = now if now is not None else time.time()
        self._evict_expired(ts)
        return sum(count for _, count in self._events)

    def get_rate(self, now: Optional[float] = None) -> float:
        """Get events per second in the window."""
        return self.get_count(now) / self.window_seconds


class TumblingWindowAggregator:
    """Fixed non-overlapping window aggregator (tumbling window)."""

    def __init__(self, window_seconds: float):
        self.window_seconds = window_seconds
        self.values: list = []
        self.window_start = time.time()

    def add(self, val: float, timestamp: Optional[float] = None) -> None:
        ts = timestamp if timestamp is not None else time.time()
        if ts - self.window_start >= self.window_seconds:
            self.values.clear()
            self.window_start = ts
        self.values.append(val)

    def get_summary(self) -> Dict[str, float]:
        if not self.values:
            return {"count": 0.0, "sum": 0.0, "avg": 0.0, "min": 0.0, "max": 0.0}
        return {
            "count": float(len(self.values)),
            "sum": float(sum(self.values)),
            "avg": float(sum(self.values) / len(self.values)),
            "min": float(min(self.values)),
            "max": float(max(self.values)),
        }
