"""Unit tests for humanize utilities."""

import unittest
from src.humanize_utils import ordinal, intcomma, natural_list


class TestHumanizeUtils(unittest.TestCase):

    def test_ordinal(self):
        self.assertEqual(ordinal(1), "1st")
        self.assertEqual(ordinal(2), "2nd")
        self.assertEqual(ordinal(3), "3rd")
        self.assertEqual(ordinal(4), "4th")
        self.assertEqual(ordinal(11), "11th")
        self.assertEqual(ordinal(12), "12th")
        self.assertEqual(ordinal(13), "13th")
        self.assertEqual(ordinal(21), "21st")
        self.assertEqual(ordinal(102), "102nd")

    def test_intcomma(self):
        self.assertEqual(intcomma(1000), "1,000")
        self.assertEqual(intcomma(1000000), "1,000,000")
        self.assertEqual(intcomma(12345.67), "12,345.67")

    def test_natural_list(self):
        self.assertEqual(natural_list([]), "")
        self.assertEqual(natural_list(["apples"]), "apples")
        self.assertEqual(natural_list(["apples", "oranges"]), "apples and oranges")
        self.assertEqual(natural_list(["apples", "oranges", "bananas"]), "apples, oranges, and bananas")


if __name__ == "__main__":
    unittest.main()
