"""Unit tests for color contrast and WCAG compliance."""

import unittest
from src.color_contrast import contrast_ratio, is_wcag_aa, is_wcag_aaa


class TestColorContrast(unittest.TestCase):

    def test_black_and_white_contrast(self):
        ratio = contrast_ratio("#ffffff", "#000000")
        self.assertEqual(ratio, 21.0)
        self.assertTrue(is_wcag_aa("#ffffff", "#000000"))
        self.assertTrue(is_wcag_aaa("#ffffff", "#000000"))

    def test_low_contrast(self):
        self.assertFalse(is_wcag_aa("#888888", "#999999"))


if __name__ == "__main__":
    unittest.main()
