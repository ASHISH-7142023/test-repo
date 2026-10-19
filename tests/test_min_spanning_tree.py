import unittest
from src.min_spanning_tree import kruskal_mst, prim_mst

class TestMinSpanningTree(unittest.TestCase):
    def test_kruskal_and_prim(self):
        v = ["A", "B", "C", "D"]
        e = [
            ("A", "B", 1.0),
            ("B", "C", 4.0),
            ("A", "C", 3.0),
            ("C", "D", 2.0),
            ("B", "D", 5.0)
        ]
        k_weight, k_edges = kruskal_mst(v, e)
        p_weight, p_edges = prim_mst(v, e)
        self.assertEqual(k_weight, 6.0)
        self.assertEqual(p_weight, 6.0)
        self.assertEqual(len(k_edges), 3)
        self.assertEqual(len(p_edges), 3)

if __name__ == "__main__":
    unittest.main()
