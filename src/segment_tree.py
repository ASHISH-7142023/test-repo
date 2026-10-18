"""Segment Tree for general associative range queries and point updates."""

from typing import Callable, List, TypeVar

T = TypeVar("T")


class SegmentTree:
    """Array-based Segment Tree supporting range queries in O(log n)."""

    def __init__(self, data: List[T], op: Callable[[T, T], T], default: T):
        self.n = len(data)
        self.op = op
        self.default = default
        self.tree: List[T] = [default] * (4 * self.n if self.n > 0 else 1)
        if self.n > 0:
            self._build(data, 0, 0, self.n - 1)

    def _build(self, data: List[T], node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = data[start]
            return
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        self._build(data, left_child, start, mid)
        self._build(data, right_child, mid + 1, end)
        self.tree[node] = self.op(self.tree[left_child], self.tree[right_child])

    def query(self, left: int, right: int) -> T:
        """Query range [left, right] inclusive (0-based)."""
        if self.n == 0 or left > right or right < 0 or left >= self.n:
            return self.default
        return self._query(0, 0, self.n - 1, max(0, left), min(self.n - 1, right))

    def _query(self, node: int, start: int, end: int, l: int, r: int) -> T:
        if r < start or end < l:
            return self.default
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self._query(2 * node + 1, start, mid, l, r)
        p2 = self._query(2 * node + 2, mid + 1, end, l, r)
        return self.op(p1, p2)

    def update(self, idx: int, value: T) -> None:
        """Update point at 0-based idx."""
        if not (0 <= idx < self.n):
            raise IndexError("Index out of bounds.")
        self._update(0, 0, self.n - 1, idx, value)

    def _update(self, node: int, start: int, end: int, idx: int, value: T) -> None:
        if start == end:
            self.tree[node] = value
            return
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        if idx <= mid:
            self._update(left_child, start, mid, idx, value)
        else:
            self._update(right_child, mid + 1, end, idx, value)
        self.tree[node] = self.op(self.tree[left_child], self.tree[right_child])
