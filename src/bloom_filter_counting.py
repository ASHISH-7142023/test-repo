"""Counting Bloom Filter implementation supporting element deletion."""

import hashlib
from typing import List


class CountingBloomFilter:
    """Probabilistic data structure with deletion and frequency counting."""

    def __init__(self, size: int = 500, num_hashes: int = 3):
        if size <= 0 or num_hashes <= 0:
            raise ValueError("Size and num_hashes must be positive integers.")
        self.size = size
        self.num_hashes = num_hashes
        self.counts: List[int] = [0] * size

    def _hashes(self, item: str) -> List[int]:
        indexes = []
        for seed in range(self.num_hashes):
            data = f"{seed}:{item}".encode("utf-8")
            h = int(hashlib.md5(data).hexdigest(), 16)
            indexes.append(h % self.size)
        return indexes

    def add(self, item: str) -> None:
        """Add item by incrementing counters at hashed indices."""
        for idx in self._hashes(item):
            self.counts[idx] += 1

    def remove(self, item: str) -> bool:
        """Remove item by decrementing counters. Returns False if item definitely not in filter."""
        if not self.contains(item):
            return False
        for idx in self._hashes(item):
            if self.counts[idx] > 0:
                self.counts[idx] -= 1
        return True

    def contains(self, item: str) -> bool:
        """Check if item might be in filter (all hash positions > 0)."""
        return all(self.counts[idx] > 0 for idx in self._hashes(item))

    def count(self, item: str) -> int:
        """Get minimum counter value across hash locations."""
        return min(self.counts[idx] for idx in self._hashes(item))
