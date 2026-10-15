"""Unit tests for CircuitBreaker resilience pattern."""

import time
import unittest
from src.circuit_breaker import CircuitBreaker, CircuitBreakerOpenException


class TestCircuitBreaker(unittest.TestCase):

    def test_trips_to_open_after_threshold(self):
        cb = CircuitBreaker(failure_threshold=2, recovery_timeout=0.1)

        def failing():
            raise RuntimeError("Backend down")

        # First failure
        with self.assertRaises(RuntimeError):
            cb.call(failing)
        # Second failure (trips)
        with self.assertRaises(RuntimeError):
            cb.call(failing)

        # Third attempt should be rejected by circuit breaker immediately
        with self.assertRaises(CircuitBreakerOpenException):
            cb.call(failing)

    def test_recovery_in_half_open(self):
        cb = CircuitBreaker(failure_threshold=1, recovery_timeout=0.05)
        with self.assertRaises(RuntimeError):
            cb.call(lambda: (_ for _ in ()).throw(RuntimeError("error")))

        time.sleep(0.06)
        # Succeeds in half open, circuit resets
        res = cb.call(lambda: "healthy")
        self.assertEqual(res, "healthy")
        self.assertEqual(cb.state, CircuitBreaker.STATE_CLOSED)


if __name__ == "__main__":
    unittest.main()
