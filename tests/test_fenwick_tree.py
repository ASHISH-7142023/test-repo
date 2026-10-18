import unittest
from src.fenwick_tree import FenwickTree

class TestFenwickTree(unittest.TestCase):
    def test_prefix_and_range_sum(self):
        ft = FenwickTree.from_list([1, 2, 3, 4, 5])
        self.assertEqual(ft.prefix_sum(3), 6)
        self.assertEqual(ft.range_sum(2, 4), 9)

    def test_point_update(self):
        ft = FenwickTree.from_list([10, 20, 30])
        ft.update(2, 5)
        self.assertEqual(ft.range_sum(1, 2), 35)
        self.assertEqual(ft.range_sum(2, 3), 55)

if __name__ == "__main__":
    unittest.main()
