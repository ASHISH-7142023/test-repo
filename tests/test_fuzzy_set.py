import unittest
from src.fuzzy_set import TriangularMembership, FuzzySet

class TestFuzzySet(unittest.TestCase):
    def test_triangular_membership(self):
        tri = TriangularMembership(0, 10, 20)
        f = FuzzySet(tri)
        self.assertEqual(f(10), 1.0)
        self.assertEqual(f(5), 0.5)
        self.assertEqual(f(15), 0.5)
        self.assertEqual(f(0), 0.0)
        self.assertEqual(f(25), 0.0)

    def test_fuzzy_operations(self):
        f1 = FuzzySet(lambda x: 0.8)
        f2 = FuzzySet(lambda x: 0.3)
        self.assertAlmostEqual(f1.union(f2)(0), 0.8)
        self.assertAlmostEqual(f1.intersection(f2)(0), 0.3)
        self.assertAlmostEqual(f1.complement()(0), 0.2)

if __name__ == "__main__":
    unittest.main()
