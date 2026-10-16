"""Unit tests for DisjointSet (Union-Find)."""

import unittest
from src.disjoint_set import DisjointSet


class TestDisjointSet(unittest.TestCase):

    def test_union_and_connected(self):
        ds = DisjointSet()
        ds.union(1, 2)
        ds.union(2, 3)
        ds.union(4, 5)

        self.assertTrue(ds.connected(1, 3))
        self.assertTrue(ds.connected(4, 5))
        self.assertFalse(ds.connected(1, 4))


if __name__ == "__main__":
    unittest.main()
