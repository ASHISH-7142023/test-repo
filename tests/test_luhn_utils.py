"""Unit tests for Luhn algorithm utilities."""

import unittest
from src.luhn_utils import validate_luhn, calculate_luhn_digit


class TestLuhnUtils(unittest.TestCase):

    def test_validate_luhn_valid_cases(self):
        self.assertTrue(validate_luhn("49927398716"))
        self.assertTrue(validate_luhn("79927398713"))

    def test_validate_luhn_invalid(self):
        self.assertFalse(validate_luhn("49927398717"))
        self.assertFalse(validate_luhn("abc123"))

    def test_calculate_luhn_digit(self):
        # 7992739871 + 3 satisfies Luhn
        check_digit = calculate_luhn_digit("7992739871")
        self.assertEqual(check_digit, 3)


if __name__ == "__main__":
    unittest.main()
