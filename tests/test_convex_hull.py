import unittest
from src.convex_hull import Point2D, convex_hull_graham, polygon_area

class TestConvexHull(unittest.TestCase):
    def test_square_with_interior_point(self):
        pts = [
            (0, 0), (4, 0), (4, 4), (0, 4), (2, 2)
        ]
        hull = convex_hull_graham(pts)
        self.assertEqual(len(hull), 4)
        area = polygon_area(hull)
        self.assertEqual(area, 16.0)

    def test_collinear_points(self):
        pts = [(0, 0), (1, 1), (2, 2), (3, 3)]
        hull = convex_hull_graham(pts)
        self.assertEqual(len(hull), 2)

if __name__ == "__main__":
    unittest.main()
