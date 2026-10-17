"""Interval Tree data structure for 1D range intersection queries."""

from typing import Any, List, Optional


class Interval:
    def __init__(self, start: float, end: float, data: Any = None):
        if start > end:
            raise ValueError(f"Invalid interval: start ({start}) cannot exceed end ({end}).")
        self.start = start
        self.end = end
        self.data = data

    def overlaps(self, start: float, end: float) -> bool:
        return self.start <= end and self.end >= start

    def contains_point(self, point: float) -> bool:
        return self.start <= point <= self.end

    def __repr__(self) -> str:
        return f"Interval({self.start}, {self.end}, data={self.data!r})"


class IntervalTreeNode:
    def __init__(self, interval: Interval):
        self.interval = interval
        self.max_end = interval.end
        self.left: Optional["IntervalTreeNode"] = None
        self.right: Optional["IntervalTreeNode"] = None


class IntervalTree:
    """Interval tree for fast interval stabbing and overlap searches."""

    def __init__(self):
        self.root: Optional[IntervalTreeNode] = None
        self._size = 0

    def insert(self, start: float, end: float, data: Any = None) -> None:
        interval = Interval(start, end, data)
        self.root = self._insert_node(self.root, interval)
        self._size += 1

    def _insert_node(self, node: Optional[IntervalTreeNode], interval: Interval) -> IntervalTreeNode:
        if node is None:
            return IntervalTreeNode(interval)

        if interval.start < node.interval.start:
            node.left = self._insert_node(node.left, interval)
        else:
            node.right = self._insert_node(node.right, interval)

        node.max_end = max(node.max_end, interval.end)
        return node

    def find_overlapping(self, start: float, end: float) -> List[Interval]:
        results: List[Interval] = []
        self._search_overlap(self.root, start, end, results)
        return results

    def _search_overlap(self, node: Optional[IntervalTreeNode], start: float, end: float, res: List[Interval]) -> None:
        if node is None:
            return

        if node.interval.overlaps(start, end):
            res.append(node.interval)

        if node.left and node.left.max_end >= start:
            self._search_overlap(node.left, start, end, res)

        if node.right and node.interval.start <= end:
            self._search_overlap(node.right, start, end, res)

    def find_at_point(self, point: float) -> List[Interval]:
        return self.find_overlapping(point, point)

    def __len__(self) -> int:
        return self._size
