import unittest
from src.hungarian_algorithm import hungarian_min_assignment

class TestHungarianAlgorithm(unittest.TestCase):
    def test_optimal_assignment(self):
        matrix = [
            [4.0, 1.0, 3.0],
            [2.0, 0.0, 5.0],
            [3.0, 2.0, 2.0]
        ]
        cost, pairs = hungarian_min_assignment(matrix)
        self.assertEqual(cost, 5.0)
        self.assertEqual(len(pairs), 3)

if __name__ == "__main__":
    unittest.main()
