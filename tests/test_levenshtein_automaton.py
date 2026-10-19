import unittest
from src.levenshtein_automaton import levenshtein_distance, fuzzy_search, LevenshteinAutomaton

class TestLevenshteinAutomaton(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(levenshtein_distance("kitten", "sitting"), 3)
        self.assertEqual(levenshtein_distance("hello", "hello"), 0)
        self.assertEqual(levenshtein_distance("", "abc"), 3)

    def test_fuzzy_dictionary_search(self):
        dictionary = ["apple", "apply", "ape", "ample", "banana", "maple"]
        matches = fuzzy_search("apple", 1, dictionary)
        words = [w for w, d in matches]
        self.assertIn("apple", words)
        self.assertIn("apply", words)
        self.assertIn("ample", words)
        self.assertNotIn("banana", words)

if __name__ == "__main__":
    unittest.main()
