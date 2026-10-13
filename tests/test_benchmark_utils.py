"""Unit tests for benchmarking and profiling utilities."""

import time
import unittest
from src.benchmark_utils import BenchmarkTimer, timed, benchmark_function


class TestBenchmarkUtils(unittest.TestCase):

    def test_benchmark_timer_context(self):
        with BenchmarkTimer("sleep_test") as timer:
            time.sleep(0.02)
        self.assertGreaterEqual(timer.elapsed, 0.015)
        self.assertGreaterEqual(timer.elapsed_ms, 15.0)

    def test_timed_decorator(self):
        reported = {}

        def record(name, elapsed):
            reported["name"] = name
            reported["elapsed"] = elapsed

        @timed(callback=record)
        def sample_work():
            time.sleep(0.01)
            return "done"

        result = sample_work()
        self.assertEqual(result, "done")
        self.assertEqual(reported["name"], "sample_work")
        self.assertGreater(reported["elapsed"], 0.0)

    def test_benchmark_function(self):
        def simple_computation():
            _ = sum(range(1000))

        stats = benchmark_function(simple_computation, iterations=5)
        self.assertEqual(stats["iterations"], 5.0)
        self.assertGreater(stats["total_seconds"], 0.0)
        self.assertGreater(stats["mean_seconds"], 0.0)
        self.assertGreaterEqual(stats["max_seconds"], stats["min_seconds"])


if __name__ == "__main__":
    unittest.main()
