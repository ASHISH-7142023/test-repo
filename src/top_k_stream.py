"""Streaming Top-K items counter and leaderboard tracker."""

import heapq
from typing import Any, List, Tuple


class TopKStream:
    """Maintains the top K highest scored items in an incoming data stream."""

    def __init__(self, k: int):
        if k <= 0:
            raise ValueError("k must be greater than zero.")
        self.k = k
        self._heap: List[Tuple[float, int, Any]] = []
        self._count = 0

    def add(self, item: Any, score: float) -> None:
        """Process item with associated score."""
        entry = (score, self._count, item)
        self._count += 1
        if len(self._heap) < self.k:
            heapq.heappush(self._heap, entry)
        elif score > self._heap[0][0]:
            heapq.heapreplace(self._heap, entry)

    def get_top_k(self) -> List[Any]:
        """Return top K items in descending score order."""
        sorted_entries = sorted(self._heap, key=lambda x: x[0], reverse=True)
        return [item for _, _, item in sorted_entries]
