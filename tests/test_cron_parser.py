import unittest
from datetime import datetime
from src.cron_parser import parse_cron_field, parse_cron, matches_cron, explain_cron

class TestCronParser(unittest.TestCase):
    def test_parse_field(self):
        self.assertEqual(parse_cron_field("*/15", 0, 59), {0, 15, 30, 45})
        self.assertEqual(parse_cron_field("1-3,5", 0, 10), {1, 2, 3, 5})

    def test_matching(self):
        dt = datetime(2026, 10, 19, 14, 30)
        self.assertTrue(matches_cron("30 14 * * 1", dt))
        self.assertFalse(matches_cron("0 14 * * 1", dt))

    def test_explain(self):
        explanation = explain_cron("*/10 9-17 * * 1-5")
        self.assertIn("Every 10 minutes", explanation)

if __name__ == "__main__":
    unittest.main()
