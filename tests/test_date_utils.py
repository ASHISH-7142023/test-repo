"""Unit tests for date utilities."""

import unittest
from datetime import datetime, timezone
from src.date_utils import format_iso, human_readable_duration, days_between, is_leap_year


class TestDateUtils(unittest.TestCase):

    def test_format_iso(self):
        dt = datetime(2026, 10, 12, 14, 30, 0, tzinfo=timezone.utc)
        self.assertEqual(format_iso(dt), "2026-10-12T14:30:00Z")

    def test_human_readable_duration(self):
        self.assertEqual(human_readable_duration(45), "45s")
        self.assertEqual(human_readable_duration(125), "2m 5s")
        self.assertEqual(human_readable_duration(3600), "1h")
        self.assertEqual(human_readable_duration(90000), "1d 1h")
        self.assertEqual(human_readable_duration(-5), "0s")

    def test_days_between(self):
        self.assertEqual(days_between("2026-01-01", "2026-01-10"), 9)
        self.assertEqual(days_between("2026-12-31", "2026-12-31"), 0)

    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(2024))
        self.assertFalse(is_leap_year(2026))
        self.assertTrue(is_leap_year(2000))
        self.assertFalse(is_leap_year(1900))


if __name__ == "__main__":
    unittest.main()
