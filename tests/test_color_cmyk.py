import unittest
from src.color_cmyk import rgb_to_cmyk, cmyk_to_rgb

class TestColorCMYK(unittest.TestCase):
    def test_pure_colors(self):
        self.assertEqual(rgb_to_cmyk(0, 0, 0), (0.0, 0.0, 0.0, 100.0))
        self.assertEqual(rgb_to_cmyk(255, 255, 255), (0.0, 0.0, 0.0, 0.0))
        self.assertEqual(rgb_to_cmyk(255, 0, 0), (0.0, 100.0, 100.0, 0.0))

    def test_roundtrip(self):
        r, g, b = 100, 150, 200
        c, m, y, k = rgb_to_cmyk(r, g, b)
        r2, g2, b2 = cmyk_to_rgb(c, m, y, k)
        self.assertAlmostEqual(r, r2, delta=1)
        self.assertAlmostEqual(g, g2, delta=1)
        self.assertAlmostEqual(b, b2, delta=1)

if __name__ == "__main__":
    unittest.main()
