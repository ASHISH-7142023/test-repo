import unittest
from src.suffix_array import build_suffix_array, suffix_array_search, longest_repeated_substring

class TestSuffixArray(unittest.TestCase):
    def test_suffix_array_order(self):
        text = "banana"
        sa = build_suffix_array(text)
        self.assertEqual(sa, [5, 3, 1, 0, 4, 2])

    def test_suffix_array_search(self):
        text = "abracadabra"
        matches = suffix_array_search(text, "abra")
        self.assertEqual(matches, [0, 7])

    def test_longest_repeated_substring(self):
        self.assertEqual(longest_repeated_substring("banana"), "ana")
        self.assertEqual(longest_repeated_substring("abcdef"), "")

if __name__ == "__main__":
    unittest.main()
