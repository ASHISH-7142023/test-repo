import unittest
from src.kd_tree import KDTree

class TestKDTree(unittest.TestCase):
    def test_nearest_neighbor(self):
        pts = [(2.0, 3.0), (5.0, 4.0), (9.0, 6.0), (4.0, 7.0), (8.0, 1.0), (7.0, 2.0)]
        tree = KDTree(pts, dimensions=2)
        closest, dist = tree.nearest_neighbor((9.0, 2.0))
        self.assertEqual(closest, (8.0, 1.0))

    def test_range_query(self):
        pts = [(1.0, 1.0), (2.0, 2.0), (3.0, 3.0), (10.0, 10.0)]
        tree = KDTree(pts, dimensions=2)
        in_box = tree.range_query((0.0, 0.0), (3.5, 3.5))
        self.assertEqual(len(in_box), 3)
        self.assertNotIn((10.0, 10.0), in_box)

if __name__ == "__main__":
    unittest.main()
