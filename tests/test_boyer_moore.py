import unittest
from src.boyer_moore import build_bad_char_table, boyer_moore_search, boyer_moore_contains

class TestBoyerMoore(unittest.TestCase):
    def test_bad_char_table(self):
        table = build_bad_char_table("NEEDLE")
        self.assertEqual(table["N"], 0)
        self.assertEqual(table["E"], 5)
        self.assertEqual(table["D"], 3)
        self.assertEqual(table["L"], 4)

    def test_search_occurrences(self):
        text = "FINDINAHAYSTACKNEEDLEINA"
        pattern = "NEEDLE"
        matches = boyer_moore_search(text, pattern)
        self.assertEqual(matches, [15])

    def test_repeated_patterns(self):
        matches = boyer_moore_search("banana", "an")
        self.assertEqual(matches, [1, 3])

    def test_not_found_and_contains(self):
        self.assertEqual(boyer_moore_search("hello world", "galaxy"), [])
        self.assertTrue(boyer_moore_contains("rust python go", "python"))
        self.assertFalse(boyer_moore_contains("rust python go", "java"))

if __name__ == "__main__":
    unittest.main()
