import unittest
from src.kmp_search import compute_lps, kmp_search, kmp_contains

class TestKMPSearch(unittest.TestCase):
    def test_lps_computation(self):
        self.assertEqual(compute_lps("AAAA"), [0, 1, 2, 3])
        self.assertEqual(compute_lps("ABCDE"), [0, 0, 0, 0, 0])
        self.assertEqual(compute_lps("AABAACAABAA"), [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5])

    def test_kmp_search_multiple_matches(self):
        text = "AABAACAADAABAABA"
        pattern = "AABA"
        matches = kmp_search(text, pattern)
        self.assertEqual(matches, [0, 9, 12])

    def test_kmp_search_no_match(self):
        self.assertEqual(kmp_search("hello world", "xyz"), [])

    def test_kmp_contains(self):
        self.assertTrue(kmp_contains("hello world", "world"))
        self.assertTrue(kmp_contains("hello", ""))
        self.assertFalse(kmp_contains("hello", "universe"))

if __name__ == "__main__":
    unittest.main()
