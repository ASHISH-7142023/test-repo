"""Unit tests for currency formatting utilities."""

import unittest
from src.currency_utils import format_currency, is_valid_currency_code


class TestCurrencyUtils(unittest.TestCase):

    def test_is_valid_currency_code(self):
        self.assertTrue(is_valid_currency_code("USD"))
        self.assertTrue(is_valid_currency_code("INR"))
        self.assertFalse(is_valid_currency_code("usd"))
        self.assertFalse(is_valid_currency_code("US1"))

    def test_format_currency(self):
        self.assertEqual(format_currency(1234.5, "USD"), "$1,234.50")
        self.assertEqual(format_currency(1000000, "INR"), "₹1,000,000.00")
        self.assertEqual(format_currency(99.9, "EUR", include_symbol=False), "99.90 EUR")


if __name__ == "__main__":
    unittest.main()
