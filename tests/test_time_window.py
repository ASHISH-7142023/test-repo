import unittest
from src.time_window import SlidingWindowCounter, TumblingWindowAggregator

class TestTimeWindow(unittest.TestCase):
    def test_sliding_window_expiration(self):
        sw = SlidingWindowCounter(window_seconds=10.0)
        sw.record(count=2, timestamp=100.0)
        sw.record(count=3, timestamp=105.0)

        self.assertEqual(sw.get_count(now=108.0), 5)
        self.assertEqual(sw.get_count(now=112.0), 3)

    def test_tumbling_window(self):
        tw = TumblingWindowAggregator(window_seconds=5.0)
        tw.window_start = 100.0
        tw.add(10.0, timestamp=101.0)
        tw.add(20.0, timestamp=102.0)
        summary = tw.get_summary()
        self.assertEqual(summary["count"], 2.0)
        self.assertEqual(summary["avg"], 15.0)

if __name__ == "__main__":
    unittest.main()
