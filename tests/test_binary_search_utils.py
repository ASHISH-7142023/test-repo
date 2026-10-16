"""Unit tests for binary search algorithms."""

import unittest
from src.binary_search_utils import binary_search, search_range


class TestBinarySearchUtils(unittest.TestCase):

    def test_binary_search(self):
        arr = [10, 20, 30, 40, 50]
        self.assertEqual(binary_search(arr, 30), 2)
        self.assertEqual(binary_search(arr, 99), -1)

    def test_search_range(self):
        arr = [5, 7, 7, 8, 8, 8, 10]
        self.assertEqual(search_range(arr, 8), (3, 5))
        self.assertEqual(search_range(arr, 6), (-1, -1))


if __name__ == "__main__":
    unittest.main()
