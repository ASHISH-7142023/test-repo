import unittest
from src.natural_sort import natural_sort

class TestNaturalSort(unittest.TestCase):
    def test_alphanumeric_sorting(self):
        files = ["file10.txt", "file2.txt", "file1.txt", "file20.txt"]
        self.assertEqual(natural_sort(files), ["file1.txt", "file2.txt", "file10.txt", "file20.txt"])

    def test_version_numbers(self):
        versions = ["v1.10.0", "v1.2.0", "v1.1.0"]
        self.assertEqual(natural_sort(versions), ["v1.1.0", "v1.2.0", "v1.10.0"])

if __name__ == "__main__":
    unittest.main()
