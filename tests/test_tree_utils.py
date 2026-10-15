"""Unit tests for tree data structures and traversal algorithms."""

import unittest
from src.tree_utils import TreeNode, dfs_traverse, bfs_traverse, find_node


class TestTreeUtils(unittest.TestCase):

    def setUp(self):
        # Tree:
        #       1
        #     /   \
        #    2     3
        #   / \
        #  4   5
        self.root = TreeNode(1)
        n2 = self.root.add_child(TreeNode(2))
        self.root.add_child(TreeNode(3))
        n2.add_child(TreeNode(4))
        n2.add_child(TreeNode(5))

    def test_dfs_traverse(self):
        vals = dfs_traverse(self.root)
        self.assertEqual(vals, [1, 2, 4, 5, 3])

    def test_bfs_traverse(self):
        vals = bfs_traverse(self.root)
        self.assertEqual(vals, [1, 2, 3, 4, 5])

    def test_find_node(self):
        found = find_node(self.root, lambda v: v == 5)
        self.assertIsNotNone(found)
        self.assertEqual(found.val, 5)

        missing = find_node(self.root, lambda v: v == 99)
        self.assertIsNone(missing)


if __name__ == "__main__":
    unittest.main()
