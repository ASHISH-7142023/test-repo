import unittest
from src.roman_numerals import to_roman, from_roman

class TestRomanNumerals(unittest.TestCase):
    def test_to_roman(self):
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(1984), "MCMLXXXIV")
        self.assertEqual(to_roman(2026), "MMXXVI")

    def test_from_roman(self):
        self.assertEqual(from_roman("MCMLXXXIV"), 1984)
        self.assertEqual(from_roman("MMXXVI"), 2026)

    def test_invalid_cases(self):
        with self.assertRaises(ValueError):
            to_roman(0)
        with self.assertRaises(ValueError):
            from_roman("IIII")

if __name__ == "__main__":
    unittest.main()
