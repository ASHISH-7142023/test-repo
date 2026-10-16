"""Unit tests for Trie prefix tree."""

import unittest
from src.trie_utils import Trie


class TestTrieUtils(unittest.TestCase):

    def test_insert_and_search(self):
        trie = Trie()
        trie.insert("python")
        trie.insert("pytest")

        self.assertTrue(trie.search("python"))
        self.assertTrue(trie.search("pytest"))
        self.assertFalse(trie.search("py"))
        self.assertTrue(trie.starts_with("py"))

    def test_autocomplete(self):
        trie = Trie()
        for word in ["apple", "app", "application", "banana"]:
            trie.insert(word)

        matches = trie.autocomplete("app")
        self.assertEqual(matches, ["app", "apple", "application"])


if __name__ == "__main__":
    unittest.main()
