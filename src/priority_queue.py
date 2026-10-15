"""Thread-safe priority queue implementation using binary heap."""

import heapq
import threading
from typing import Any, Tuple, Optional


class PriorityQueue:
    """Thread-safe priority queue returning lowest priority value first."""

    def __init__(self):
        self._heap = []
        self._count = 0
        self._lock = threading.Lock()

    def push(self, item: Any, priority: float) -> None:
        """Insert item with numeric priority."""
        with self._lock:
            # count ensures deterministic FIFO ordering for duplicate priorities
            heapq.heappush(self._heap, (priority, self._count, item))
            self._count += 1

    def pop(self) -> Any:
        """Remove and return item with lowest priority number."""
        with self._lock:
            if not self._heap:
                raise IndexError("Cannot pop from empty PriorityQueue.")
            _, _, item = heapq.heappop(self._heap)
            return item

    def peek(self) -> Optional[Any]:
        """View next lowest priority item without popping."""
        with self._lock:
            return self._heap[0][2] if self._heap else None

    def __len__(self) -> int:
        with self._lock:
            return len(self._heap)
