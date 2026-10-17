import unittest
from src.color_hsl import rgb_to_hsl, hsl_to_rgb, hex_to_hsl, hsl_to_hex

class TestColorHSL(unittest.TestCase):
    def test_pure_colors(self):
        self.assertEqual(rgb_to_hsl(255, 0, 0), (0.0, 100.0, 50.0))
        self.assertEqual(hsl_to_rgb(0, 100, 50), (255, 0, 0))

        self.assertEqual(rgb_to_hsl(0, 255, 0), (120.0, 100.0, 50.0))
        self.assertEqual(hsl_to_rgb(120, 100, 50), (0, 255, 0))

        self.assertEqual(rgb_to_hsl(0, 0, 255), (240.0, 100.0, 50.0))
        self.assertEqual(hsl_to_rgb(240, 100, 50), (0, 0, 255))

    def test_hex_conversion(self):
        hsl = hex_to_hsl("#ffffff")
        self.assertEqual(hsl[2], 100.0)
        self.assertEqual(hsl_to_hex(0, 0, 100), "#ffffff")
        self.assertEqual(hsl_to_hex(0, 0, 0), "#000000")

if __name__ == "__main__":
    unittest.main()
