"""Unit tests for BloomFilter probabilistic data structure."""

import unittest
from src.bloom_filter import BloomFilter


class TestBloomFilter(unittest.TestCase):

    def test_bloom_filter_membership(self):
        bf = BloomFilter(capacity=100, error_rate=0.01)
        bf.add("apple")
        bf.add("banana")

        self.assertTrue("apple" in bf)
        self.assertTrue("banana" in bf)
        self.assertFalse("orange" in bf)


if __name__ == "__main__":
    unittest.main()
