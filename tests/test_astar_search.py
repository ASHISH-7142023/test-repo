import unittest
from src.astar_search import astar_grid

class TestAStar(unittest.TestCase):
    def test_simple_path(self):
        grid = [
            [0, 0, 0],
            [1, 1, 0],
            [0, 0, 0]
        ]
        path, cost = astar_grid(grid, (0, 0), (2, 0))
        self.assertEqual(cost, 6.0)
        self.assertEqual(path[0], (0, 0))
        self.assertEqual(path[-1], (2, 0))

    def test_blocked_path(self):
        grid = [
            [0, 1],
            [1, 0]
        ]
        path, cost = astar_grid(grid, (0, 0), (1, 1))
        self.assertEqual(path, [])
        self.assertEqual(cost, float("inf"))

if __name__ == "__main__":
    unittest.main()
