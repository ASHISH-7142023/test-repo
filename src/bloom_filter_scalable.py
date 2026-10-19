"""
Scalable Bloom Filter (Zero-dependency).
Automatically scales by adding sub-filters as capacity fills,
tightening the error probability of subsequent filters to bound the cumulative error rate.
"""
import math
import hashlib
from typing import Any, List

class _BloomFilterPart:
    def __init__(self, capacity: int, error_rate: float):
        self.capacity = max(1, capacity)
        self.error_rate = error_rate
        # Optimal number of bits m = - (n * ln(p)) / (ln(2)^2)
        self.size = max(8, int(- (self.capacity * math.log(self.error_rate)) / (math.log(2) ** 2)))
        # Optimal number of hash functions k = (m / n) * ln(2)
        self.num_hashes = max(1, int((self.size / self.capacity) * math.log(2)))
        self.bit_array = bytearray((self.size + 7) // 8)
        self.count = 0

    def _hashes(self, item_bytes: bytes):
        h1 = int(hashlib.sha256(item_bytes).hexdigest()[:16], 16)
        h2 = int(hashlib.sha256(item_bytes + b"\x01").hexdigest()[:16], 16)
        step = (h2 % (self.size - 1)) + 1 if self.size > 1 else 1
        for i in range(self.num_hashes):
            yield (h1 + i * step) % self.size

    def add(self, item_bytes: bytes) -> bool:
        new_bit = False
        for bit_idx in self._hashes(item_bytes):
            byte_idx = bit_idx // 8
            bit_mask = 1 << (bit_idx % 8)
            if not (self.bit_array[byte_idx] & bit_mask):
                self.bit_array[byte_idx] |= bit_mask
                new_bit = True
        self.count += 1
        return new_bit

    def contains(self, item_bytes: bytes) -> bool:
        for bit_idx in self._hashes(item_bytes):
            byte_idx = bit_idx // 8
            bit_mask = 1 << (bit_idx % 8)
            if not (self.bit_array[byte_idx] & bit_mask):
                return False
        return True

class ScalableBloomFilter:
    """
    Scalable Bloom Filter that adds new sub-filters as capacity is reached.
    """
    def __init__(self, initial_capacity: int = 100, error_rate: float = 0.01, scale_factor: int = 2, tightening_ratio: float = 0.85):
        if initial_capacity <= 0:
            raise ValueError("initial_capacity must be > 0")
        if not (0 < error_rate < 1):
            raise ValueError("error_rate must be between 0 and 1")
        self.initial_capacity = initial_capacity
        self.error_rate = error_rate
        self.scale_factor = scale_factor
        self.tightening_ratio = tightening_ratio
        self.filters: List[_BloomFilterPart] = [
            _BloomFilterPart(self.initial_capacity, self.error_rate * (1 - self.tightening_ratio))
        ]
        self._total_count = 0

    def _to_bytes(self, item: Any) -> bytes:
        if isinstance(item, bytes):
            return item
        return str(item).encode("utf-8")

    def add(self, item: Any) -> None:
        item_bytes = self._to_bytes(item)
        active = self.filters[-1]
        if active.count >= active.capacity:
            next_cap = active.capacity * self.scale_factor
            next_err = active.error_rate * self.tightening_ratio
            active = _BloomFilterPart(next_cap, next_err)
            self.filters.append(active)
        active.add(item_bytes)
        self._total_count += 1

    def __contains__(self, item: Any) -> bool:
        item_bytes = self._to_bytes(item)
        for f in reversed(self.filters):
            if f.contains(item_bytes):
                return True
        return False

    def __len__(self) -> int:
        return self._total_count

    @property
    def num_filters(self) -> int:
        return len(self.filters)
