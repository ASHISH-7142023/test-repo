"""Unit tests for Levenshtein distance and string similarity."""

import unittest
from src.levenshtein_utils import levenshtein_distance, similarity_ratio, find_closest_match


class TestLevenshteinUtils(unittest.TestCase):

    def test_levenshtein_distance(self):
        self.assertEqual(levenshtein_distance("kitten", "sitting"), 3)
        self.assertEqual(levenshtein_distance("flaw", "lawn"), 2)
        self.assertEqual(levenshtein_distance("same", "same"), 0)

    def test_similarity_ratio(self):
        self.assertEqual(similarity_ratio("hello", "hello"), 1.0)
        self.assertGreater(similarity_ratio("test", "text"), 0.7)

    def test_find_closest_match(self):
        candidates = ["apple", "banana", "orange"]
        best = find_closest_match("appel", candidates)
        self.assertEqual(best, "apple")


if __name__ == "__main__":
    unittest.main()
