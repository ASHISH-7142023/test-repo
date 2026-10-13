"""Unit tests for ANSI color formatting and strip utilities."""

import unittest
from src.color_utils import (
    colorize,
    rgb,
    hex_to_rgb,
    hex_color,
    strip_ansi,
    RED,
    GREEN,
    BOLD,
    RESET
)


class TestColorUtils(unittest.TestCase):

    def test_colorize(self):
        result = colorize("Success", GREEN)
        self.assertEqual(result, f"{GREEN}Success{RESET}")

    def test_rgb(self):
        result = rgb("Sky", 56, 189, 248)
        self.assertEqual(result, f"\033[38;2;56;189;248mSky{RESET}")

    def test_hex_to_rgb(self):
        self.assertEqual(hex_to_rgb("#ffffff"), (255, 255, 255))
        self.assertEqual(hex_to_rgb("000000"), (0, 0, 0))
        self.assertEqual(hex_to_rgb("#f00"), (255, 0, 0))

        with self.assertRaises(ValueError):
            hex_to_rgb("invalid_hex")

    def test_hex_color(self):
        res = hex_color("Ruby", "#ff0000")
        self.assertEqual(res, f"\033[38;2;255;0;0mRuby{RESET}")

    def test_strip_ansi(self):
        colored = f"{BOLD}{RED}Error occurred!{RESET}"
        self.assertEqual(strip_ansi(colored), "Error occurred!")
        self.assertEqual(strip_ansi("Normal text without codes"), "Normal text without codes")
        self.assertEqual(strip_ansi(""), "")


if __name__ == "__main__":
    unittest.main()
