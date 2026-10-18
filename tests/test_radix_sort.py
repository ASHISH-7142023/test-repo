import unittest
from src.radix_sort import counting_sort, radix_sort_integers

class TestRadixSort(unittest.TestCase):
    def test_counting_sort(self):
        self.assertEqual(counting_sort([4, 2, 2, 8, 3, 3, 1]), [1, 2, 2, 3, 3, 4, 8])

    def test_radix_sort_integers_with_negatives(self):
        arr = [170, 45, -75, 90, -802, 24, 2, 66]
        self.assertEqual(radix_sort_integers(arr), sorted(arr))

    def test_empty_and_single(self):
        self.assertEqual(radix_sort_integers([]), [])
        self.assertEqual(radix_sort_integers([42]), [42])

if __name__ == "__main__":
    unittest.main()
