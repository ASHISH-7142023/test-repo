"""Unit tests for bitwise arithmetic utilities."""

import unittest
from src.bit_utils import (
    count_set_bits,
    is_power_of_two,
    get_bit,
    set_bit,
    clear_bit,
    toggle_bit,
    to_binary_string
)


class TestBitUtils(unittest.TestCase):

    def test_count_set_bits(self):
        self.assertEqual(count_set_bits(0), 0)
        self.assertEqual(count_set_bits(7), 3)   # 111
        self.assertEqual(count_set_bits(16), 1)  # 10000

    def test_is_power_of_two(self):
        self.assertTrue(is_power_of_two(1))
        self.assertTrue(is_power_of_two(2))
        self.assertTrue(is_power_of_two(64))
        self.assertFalse(is_power_of_two(0))
        self.assertFalse(is_power_of_two(12))

    def test_bit_manipulation(self):
        # 4 = binary 0100
        val = 4
        self.assertEqual(get_bit(val, 2), 1)
        self.assertEqual(get_bit(val, 0), 0)

        # Set bit 0 -> 0101 (5)
        val = set_bit(val, 0)
        self.assertEqual(val, 5)

        # Clear bit 2 -> 0001 (1)
        val = clear_bit(val, 2)
        self.assertEqual(val, 1)

        # Toggle bit 1 -> 0011 (3)
        val = toggle_bit(val, 1)
        self.assertEqual(val, 3)

    def test_to_binary_string(self):
        self.assertEqual(to_binary_string(5, width=8), "00000101")


if __name__ == "__main__":
    unittest.main()
