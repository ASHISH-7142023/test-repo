import unittest
from src.bellman_ford import bellman_ford, shortest_path_bf

class TestBellmanFord(unittest.TestCase):
    def test_positive_and_negative_edges(self):
        v = ["A", "B", "C", "D"]
        e = [
            ("A", "B", 4.0),
            ("A", "C", 2.0),
            ("C", "B", 1.0),
            ("B", "D", 5.0),
            ("C", "D", 8.0)
        ]
        path, cost = shortest_path_bf(v, e, "A", "D")
        self.assertEqual(path, ["A", "C", "B", "D"])
        self.assertEqual(cost, 8.0)

    def test_negative_cycle_detection(self):
        v = ["X", "Y", "Z"]
        e = [
            ("X", "Y", 1.0),
            ("Y", "Z", -3.0),
            ("Z", "X", 1.0)
        ]
        dist, pred, has_cycle = bellman_ford(v, e, "X")
        self.assertTrue(has_cycle)
        with self.assertRaises(ValueError):
            shortest_path_bf(v, e, "X", "Z")

if __name__ == "__main__":
    unittest.main()
