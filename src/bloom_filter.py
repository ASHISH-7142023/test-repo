"""Probabilistic memory-efficient Bloom filter data structure."""

import math
import hashlib
from typing import List


class BloomFilter:
    """
    Bloom Filter probabilistic set for fast membership queries.
    
    :param capacity: Expected number of elements.
    :param error_rate: Acceptable false-positive probability (0 < p < 1).
    """

    def __init__(self, capacity: int = 1000, error_rate: float = 0.01):
        if capacity <= 0 or not (0 < error_rate < 1):
            raise ValueError("Invalid capacity or error_rate.")
        self.capacity = capacity
        self.error_rate = error_rate
        # Optimal bit size m = - (n * ln(p)) / (ln(2)^2)
        self.size = int(- (capacity * math.log(error_rate)) / (math.log(2) ** 2))
        # Optimal hash functions count k = (m / n) * ln(2)
        self.num_hashes = int((self.size / capacity) * math.log(2))
        self.bit_array = [False] * self.size

    def _hashes(self, item: str) -> List[int]:
        """Generate k hash indices using double hashing."""
        h1 = int(hashlib.md5(item.encode("utf-8")).hexdigest(), 16)
        h2 = int(hashlib.sha1(item.encode("utf-8")).hexdigest(), 16)
        return [(h1 + i * h2) % self.size for i in range(self.num_hashes)]

    def add(self, item: str) -> None:
        """Add item string to bloom filter."""
        for idx in self._hashes(item):
            self.bit_array[idx] = True

    def contains(self, item: str) -> bool:
        """Check if item is possibly in set (never false-negative)."""
        return all(self.bit_array[idx] for idx in self._hashes(item))

    def __contains__(self, item: str) -> bool:
        return self.contains(item)
