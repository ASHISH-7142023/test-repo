import unittest
from datetime import datetime
from src.cron_next import get_next_cron_run

class TestCronNext(unittest.TestCase):
    def test_next_minute_run(self):
        base = datetime(2026, 1, 1, 12, 5, 0)
        next_dt = get_next_cron_run("*/15 * * * *", after_dt=base)
        self.assertEqual(next_dt, datetime(2026, 1, 1, 12, 15, 0))

    def test_specific_hour_run(self):
        base = datetime(2026, 1, 1, 8, 30, 0)
        next_dt = get_next_cron_run("0 9 * * *", after_dt=base)
        self.assertEqual(next_dt, datetime(2026, 1, 1, 9, 0, 0))

if __name__ == "__main__":
    unittest.main()
