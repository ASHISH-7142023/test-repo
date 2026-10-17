"""2D Convex Hull Graham Scan algorithm and polygon calculations."""

from typing import List, Tuple, Union


class Point2D:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) -> str:
        return f"Point2D({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point2D):
            return False
        return self.x == other.x and self.y == other.y


def _cross_product_orientation(p: Point2D, q: Point2D, r: Point2D) -> float:
    """Return > 0 for counter-clockwise turn, < 0 for clockwise, 0 for collinear."""
    return (q.x - p.x) * (r.y - p.y) - (q.y - p.y) * (r.x - p.x)


def convex_hull_graham(raw_points: List[Union[Point2D, Tuple[float, float]]]) -> List[Point2D]:
    """Calculate the 2D convex hull of a set of points using Graham Scan (Monotone Chain)."""
    points: List[Point2D] = []
    for pt in raw_points:
        if isinstance(pt, Point2D):
            points.append(pt)
        else:
            points.append(Point2D(pt[0], pt[1]))

    points = sorted(points, key=lambda p: (p.x, p.y))
    if len(points) <= 2:
        return points

    lower: List[Point2D] = []
    for p in points:
        while len(lower) >= 2 and _cross_product_orientation(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper: List[Point2D] = []
    for p in reversed(points):
        while len(upper) >= 2 and _cross_product_orientation(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


def polygon_area(polygon: List[Point2D]) -> float:
    """Calculate polygon area using Shoelace formula."""
    n = len(polygon)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i].x * polygon[j].y
        area -= polygon[j].x * polygon[i].y
    return abs(area) / 2.0
