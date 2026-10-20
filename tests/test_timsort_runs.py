import unittest
from src.timsort_runs import find_natural_runs, reverse_run_slice

class TestTimsortRuns(unittest.TestCase):
    def test_run_detection(self):
        arr = [1, 2, 3, 6, 5, 4, 7, 8]
        runs = find_natural_runs(arr)
        self.assertEqual(len(runs), 3)
        self.assertFalse(runs[0][2])
        self.assertTrue(runs[1][2])

    def test_reverse_run(self):
        arr = [5, 4, 3, 2, 1]
        reverse_run_slice(arr, 0, 4)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()
