"""Unit tests for cron expression parser and matching."""

import unittest
from src.cron_utils import parse_cron_field, matches_cron


class TestCronUtils(unittest.TestCase):

    def test_parse_cron_field(self):
        self.assertEqual(parse_cron_field("5", 0, 59), {5})
        self.assertEqual(parse_cron_field("1-3", 1, 12), {1, 2, 3})
        self.assertEqual(parse_cron_field("*/15", 0, 59), {0, 15, 30, 45})

    def test_matches_cron(self):
        expr = "*/15 9-17 * * 1-5"  # Every 15 mins during 9-5 work hours Mon-Fri
        # Minute 30, Hour 10, Day 14, Month 10, Wednesday (3) -> Match
        self.assertTrue(matches_cron(expr, minute=30, hour=10, day=14, month=10, day_of_week=3))
        # Hour 20 -> No match
        self.assertFalse(matches_cron(expr, minute=30, hour=20, day=14, month=10, day_of_week=3))


if __name__ == "__main__":
    unittest.main()
