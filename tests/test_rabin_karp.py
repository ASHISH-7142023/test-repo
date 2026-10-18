import unittest
from src.rabin_karp import rabin_karp_search, rabin_karp_contains

class TestRabinKarp(unittest.TestCase):
    def test_search_matches(self):
        text = "AABAACAADAABAABA"
        pattern = "AABA"
        self.assertEqual(rabin_karp_search(text, pattern), [0, 9, 12])

    def test_contains(self):
        self.assertTrue(rabin_karp_contains("hello world", "world"))
        self.assertFalse(rabin_karp_contains("hello world", "earth"))

if __name__ == "__main__":
    unittest.main()
