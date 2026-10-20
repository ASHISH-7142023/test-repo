import unittest
from src.color_palette import (
    hex_to_rgb, rgb_to_hex,
    generate_complementary_palette,
    generate_triadic_palette,
    generate_analogous_palette
)

class TestColorPalette(unittest.TestCase):
    def test_hex_conversion(self):
        self.assertEqual(hex_to_rgb("#ff0000"), (255, 0, 0))
        self.assertEqual(rgb_to_hex(0, 255, 0), "#00ff00")

    def test_harmonies(self):
        comp = generate_complementary_palette(255, 0, 0)
        self.assertEqual(len(comp), 2)
        tri = generate_triadic_palette(0, 128, 255)
        self.assertEqual(len(tri), 3)
        ana = generate_analogous_palette(100, 200, 50)
        self.assertEqual(len(ana), 3)

if __name__ == "__main__":
    unittest.main()
