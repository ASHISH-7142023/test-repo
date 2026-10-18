import unittest
from src.bloom_filter_counting import CountingBloomFilter

class TestCountingBloomFilter(unittest.TestCase):
    def test_add_and_contains(self):
        cbf = CountingBloomFilter(200, 3)
        self.assertFalse(cbf.contains("apple"))
        cbf.add("apple")
        self.assertTrue(cbf.contains("apple"))
        self.assertFalse(cbf.contains("banana"))

    def test_remove(self):
        cbf = CountingBloomFilter(200, 3)
        cbf.add("orange")
        self.assertTrue(cbf.contains("orange"))
        self.assertTrue(cbf.remove("orange"))
        self.assertFalse(cbf.contains("orange"))
        self.assertFalse(cbf.remove("nonexistent"))

    def test_multiple_adds(self):
        cbf = CountingBloomFilter(200, 3)
        cbf.add("test")
        cbf.add("test")
        self.assertEqual(cbf.count("test"), 2)
        cbf.remove("test")
        self.assertTrue(cbf.contains("test"))
        cbf.remove("test")
        self.assertFalse(cbf.contains("test"))

if __name__ == "__main__":
    unittest.main()
