import unittest
from src.dijkstra import WeightedGraph

class TestDijkstra(unittest.TestCase):
    def test_shortest_path(self):
        g = WeightedGraph()
        g.add_edge("A", "B", 4.0)
        g.add_edge("A", "C", 2.0)
        g.add_edge("C", "B", 1.0)
        g.add_edge("B", "D", 5.0)
        g.add_edge("C", "D", 8.0)

        path, cost = g.shortest_path("A", "D")
        self.assertEqual(path, ["A", "C", "B", "D"])
        self.assertEqual(cost, 8.0)

    def test_unreachable(self):
        g = WeightedGraph()
        g.add_edge("A", "B", 1.0, directed=True)
        g.add_edge("C", "D", 2.0, directed=True)

        path, cost = g.shortest_path("A", "D")
        self.assertEqual(path, [])
        self.assertEqual(cost, float("inf"))

    def test_negative_weight_raises(self):
        g = WeightedGraph()
        with self.assertRaises(ValueError):
            g.add_edge("A", "B", -1.0)

if __name__ == "__main__":
    unittest.main()
