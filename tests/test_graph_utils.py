"""Unit tests for Graph algorithms."""

import unittest
from src.graph_utils import Graph


class TestGraphUtils(unittest.TestCase):

    def test_topological_sort(self):
        g = Graph(directed=True)
        g.add_edge("build", "test")
        g.add_edge("test", "deploy")
        order = g.topological_sort()
        self.assertEqual(order, ["build", "test", "deploy"])

    def test_shortest_path_bfs(self):
        g = Graph(directed=False)
        g.add_edge("A", "B")
        g.add_edge("B", "C")
        g.add_edge("A", "C")
        path = g.shortest_path_bfs("A", "C")
        self.assertEqual(path, ["A", "C"])


if __name__ == "__main__":
    unittest.main()
