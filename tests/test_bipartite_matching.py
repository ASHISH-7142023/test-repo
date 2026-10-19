import unittest
from src.bipartite_matching import hopcroft_karp

class TestBipartiteMatching(unittest.TestCase):
    def test_matching_assignment(self):
        u = ["u1", "u2", "u3"]
        v = ["v1", "v2", "v3"]
        e = [
            ("u1", "v1"),
            ("u1", "v2"),
            ("u2", "v1"),
            ("u3", "v2")
        ]
        size, matching = hopcroft_karp(u, v, e)
        self.assertEqual(size, 2)
        self.assertIn("u1", matching)

    def test_perfect_matching(self):
        u = ["a", "b"]
        v = ["x", "y"]
        e = [("a", "x"), ("b", "y")]
        size, matching = hopcroft_karp(u, v, e)
        self.assertEqual(size, 2)
        self.assertEqual(matching["a"], "x")
        self.assertEqual(matching["b"], "y")

if __name__ == "__main__":
    unittest.main()
