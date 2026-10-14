"""Unit tests for descriptive statistical utilities."""

import unittest
from src.stats_utils import median, percentile, interquartile_range, z_scores


class TestStatsUtils(unittest.TestCase):

    def test_median(self):
        self.assertEqual(median([1, 3, 5]), 3.0)
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        self.assertEqual(median([10]), 10.0)
        with self.assertRaises(ValueError):
            median([])

    def test_percentile(self):
        data = [15, 20, 35, 40, 50]
        self.assertEqual(percentile(data, 0), 15.0)
        self.assertEqual(percentile(data, 100), 50.0)
        self.assertEqual(percentile(data, 50), 35.0)
        with self.assertRaises(ValueError):
            percentile(data, 150)

    def test_interquartile_range(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8]
        iqr = interquartile_range(data)
        self.assertGreater(iqr, 0)

    def test_z_scores(self):
        data = [10, 10, 10]
        self.assertEqual(z_scores(data), [0.0, 0.0, 0.0])
        z = z_scores([10, 20, 30])
        self.assertEqual(len(z), 3)
        self.assertAlmostEqual(sum(z), 0.0, places=3)


if __name__ == "__main__":
    unittest.main()
