import unittest
from src.trie_radix import RadixTree

class TestRadixTree(unittest.TestCase):
    def test_insert_and_search(self):
        rt = RadixTree()
        rt.insert("romane", 1)
        rt.insert("romanus", 2)
        rt.insert("romulus", 3)
        rt.insert("rubens", 4)

        self.assertEqual(rt.search("romane"), 1)
        self.assertEqual(rt.search("romanus"), 2)
        self.assertEqual(rt.search("romulus"), 3)
        self.assertEqual(rt.search("rubens"), 4)
        self.assertIsNone(rt.search("roman"))
        self.assertEqual(len(rt), 4)

if __name__ == "__main__":
    unittest.main()
