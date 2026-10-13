"""Unit tests for token bucket rate limiter."""

import time
import unittest
from src.rate_limiter import TokenBucketRateLimiter


class TestRateLimiter(unittest.TestCase):

    def test_burst_capacity(self):
        limiter = TokenBucketRateLimiter(rate=5.0, capacity=3.0)
        self.assertTrue(limiter.allow(1.0))
        self.assertTrue(limiter.allow(1.0))
        self.assertTrue(limiter.allow(1.0))
        # Capacity exhausted
        self.assertFalse(limiter.allow(1.0))

    def test_refill_mechanism(self):
        # 10 tokens per second -> 1 token every 0.1s
        limiter = TokenBucketRateLimiter(rate=10.0, capacity=1.0)
        self.assertTrue(limiter.allow(1.0))
        self.assertFalse(limiter.allow(1.0))

        # Sleep 0.12s to allow refill of 1 token
        time.sleep(0.12)
        self.assertTrue(limiter.allow(1.0))

    def test_acquire_with_timeout(self):
        limiter = TokenBucketRateLimiter(rate=5.0, capacity=1.0)
        self.assertTrue(limiter.acquire(1.0))

        # Trying to acquire when empty with very short timeout should fail
        self.assertFalse(limiter.acquire(1.0, timeout=0.01))

        # Acquire with enough timeout should succeed
        self.assertTrue(limiter.acquire(1.0, timeout=0.3))

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):
            TokenBucketRateLimiter(rate=-1.0, capacity=5.0)
        with self.assertRaises(ValueError):
            TokenBucketRateLimiter(rate=5.0, capacity=0.0)


if __name__ == "__main__":
    unittest.main()
