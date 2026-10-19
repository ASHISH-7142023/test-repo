import unittest
from src.hilbert_curve import point_to_hilbert, hilbert_to_point

class TestHilbertCurve(unittest.TestCase):
    def test_bijection_order_2(self):
        order = 2
        grid_size = 1 << order
        for x in range(grid_size):
            for y in range(grid_size):
                d = point_to_hilbert(x, y, order)
                px, py = hilbert_to_point(d, order)
                self.assertEqual((px, py), (x, y))

    def test_bounds(self):
        with self.assertRaises(ValueError):
            point_to_hilbert(4, 4, order=2)

if __name__ == "__main__":
    unittest.main()
