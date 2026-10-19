"""
k-d Tree (k-Dimensional Binary Space Partitioning Tree).
Supports nearest neighbor queries and orthogonal range bounding box queries.
"""
import math
from typing import List, Tuple, Optional

Point = Tuple[float, ...]

class KDNode:
    def __init__(self, point: Point, axis: int, left: Optional['KDNode'] = None, right: Optional['KDNode'] = None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right

class KDTree:
    """
    k-d Tree for spatial indexing.
    """
    def __init__(self, points: Optional[List[Point]] = None, dimensions: int = 2):
        if dimensions <= 0:
            raise ValueError("dimensions must be > 0")
        self.k = dimensions
        self._count = 0
        self.root: Optional[KDNode] = None
        if points:
            self.root = self._build(list(points), depth=0)
            self._count = len(points)

    def _build(self, points: List[Point], depth: int) -> Optional[KDNode]:
        if not points:
            return None
        axis = depth % self.k
        points.sort(key=lambda p: p[axis])
        median_idx = len(points) // 2
        node = KDNode(
            point=points[median_idx],
            axis=axis,
            left=self._build(points[:median_idx], depth + 1),
            right=self._build(points[median_idx + 1:], depth + 1)
        )
        return node

    def __len__(self) -> int:
        return self._count

    def insert(self, point: Point) -> None:
        if len(point) != self.k:
            raise ValueError(f"Point must have {self.k} dimensions")
        def _ins(node: Optional[KDNode], depth: int) -> KDNode:
            if not node:
                return KDNode(point, depth % self.k)
            axis = node.axis
            if point[axis] < node.point[axis]:
                node.left = _ins(node.left, depth + 1)
            else:
                node.right = _ins(node.right, depth + 1)
            return node
        self.root = _ins(self.root, 0)
        self._count += 1

    def _distance_sq(self, p1: Point, p2: Point) -> float:
        return sum((a - b) ** 2 for a, b in zip(p1, p2))

    def nearest_neighbor(self, target: Point) -> Tuple[Optional[Point], float]:
        """Find the closest point in the tree to the target point."""
        if not self.root:
            return None, float("inf")
        if len(target) != self.k:
            raise ValueError(f"Target must have {self.k} dimensions")

        best_point: Optional[Point] = None
        best_dist_sq: float = float("inf")

        def _search(node: Optional[KDNode]):
            nonlocal best_point, best_dist_sq
            if not node:
                return
            d_sq = self._distance_sq(node.point, target)
            if d_sq < best_dist_sq:
                best_dist_sq = d_sq
                best_point = node.point

            axis = node.axis
            diff = target[axis] - node.point[axis]
            first = node.left if diff < 0 else node.right
            second = node.right if diff < 0 else node.left

            _search(first)
            if diff ** 2 < best_dist_sq:
                _search(second)

        _search(self.root)
        return best_point, math.sqrt(best_dist_sq)

    def range_query(self, lower_bounds: Point, upper_bounds: Point) -> List[Point]:
        """Find all points within the orthogonal bounding box [lower_bounds, upper_bounds]."""
        results: List[Point] = []
        def _query(node: Optional[KDNode]):
            if not node:
                return
            in_range = all(lower_bounds[i] <= node.point[i] <= upper_bounds[i] for i in range(self.k))
            if in_range:
                results.append(node.point)
            axis = node.axis
            if lower_bounds[axis] <= node.point[axis]:
                _query(node.left)
            if upper_bounds[axis] >= node.point[axis]:
                _query(node.right)
        _query(self.root)
        return results
