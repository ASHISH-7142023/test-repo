"""Unit tests for exponential backoff retry decorator."""

import unittest
from src.retry_utils import retry


class TestRetryUtils(unittest.TestCase):

    def test_successful_first_try(self):
        calls = 0

        @retry(max_attempts=3, delay=0.01)
        def succeeds_immediately():
            nonlocal calls
            calls += 1
            return "ok"

        res = succeeds_immediately()
        self.assertEqual(res, "ok")
        self.assertEqual(calls, 1)

    def test_succeeds_after_failures(self):
        calls = 0

        @retry(max_attempts=4, delay=0.01)
        def fails_twice():
            nonlocal calls
            calls += 1
            if calls < 3:
                raise ValueError("Transient error")
            return "recovered"

        res = fails_twice()
        self.assertEqual(res, "recovered")
        self.assertEqual(calls, 3)

    def test_exhausts_attempts(self):
        calls = 0

        @retry(max_attempts=3, delay=0.01)
        def always_fails():
            nonlocal calls
            calls += 1
            raise RuntimeError("Permanent failure")

        with self.assertRaises(RuntimeError):
            always_fails()
        self.assertEqual(calls, 3)


if __name__ == "__main__":
    unittest.main()
