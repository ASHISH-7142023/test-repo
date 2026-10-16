"""Unit tests for debounce and throttle decorators."""

import time
import unittest
from src.debounce_throttle import throttle


class TestDebounceThrottle(unittest.TestCase):

    def test_throttle_allows_only_one_call_within_interval(self):
        calls = 0

        @throttle(interval_seconds=0.05)
        def record_action():
            nonlocal calls
            calls += 1

        record_action()
        record_action()
        record_action()
        self.assertEqual(calls, 1)

        time.sleep(0.06)
        record_action()
        self.assertEqual(calls, 2)


if __name__ == "__main__":
    unittest.main()
