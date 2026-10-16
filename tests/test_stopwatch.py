"""Unit tests for SplitStopwatch timer."""

import time
import unittest
from src.stopwatch import SplitStopwatch


class TestSplitStopwatch(unittest.TestCase):

    def test_stopwatch_laps(self):
        sw = SplitStopwatch()
        sw.start()
        time.sleep(0.01)
        l1 = sw.lap()
        time.sleep(0.01)
        total = sw.stop()

        self.assertGreaterEqual(l1, 0.008)
        self.assertGreaterEqual(total, 0.018)

        stats = sw.summary()
        self.assertEqual(stats["laps"], 2.0)
        self.assertGreater(stats["avg_lap"], 0.0)


if __name__ == "__main__":
    unittest.main()
