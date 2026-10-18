"""Binary Indexed Tree (Fenwick Tree) for prefix sum queries and point updates."""

from typing import List, Union

Number = Union[int, float]


class FenwickTree:
    """1-indexed Fenwick Tree supporting O(log n) prefix sums and point updates."""

    def __init__(self, size: int):
        if size <= 0:
            raise ValueError("Size must be positive integer.")
        self.size = size
        self.tree: List[Number] = [0] * (size + 1)

    @classmethod
    def from_list(cls, values: List[Number]) -> "FenwickTree":
        ft = cls(len(values))
        for i, val in enumerate(values):
            ft.update(i + 1, val)
        return ft

    def update(self, idx: int, delta: Number) -> None:
        """Add delta to element at 1-based index idx."""
        if not (1 <= idx <= self.size):
            raise IndexError("Index out of bounds.")
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & (-idx)

    def prefix_sum(self, idx: int) -> Number:
        """Compute sum of elements from index 1 to idx inclusive."""
        if idx <= 0:
            return 0
        idx = min(idx, self.size)
        total: Number = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & (-idx)
        return total

    def range_sum(self, left: int, right: int) -> Number:
        """Compute sum in range [left, right] inclusive (1-based)."""
        if left > right:
            return 0
        return self.prefix_sum(right) - self.prefix_sum(left - 1)
