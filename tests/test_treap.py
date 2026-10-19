import unittest
from src.treap import Treap

class TestTreap(unittest.TestCase):
    def test_treap_inorder_and_kth(self):
        t = Treap()
        values = [50, 20, 70, 10, 30, 60, 80]
        for v in values:
            t.insert(v)
        self.assertEqual(t.inorder(), sorted(values))
        self.assertEqual(len(t), len(values))
        self.assertEqual(t.kth_smallest(1), 10)
        self.assertEqual(t.kth_smallest(4), 50)
        self.assertEqual(t.kth_smallest(7), 80)
        self.assertIsNone(t.kth_smallest(99))

    def test_search_and_remove(self):
        t = Treap()
        t.insert(100, value="hundred")
        self.assertEqual(t.search(100), "hundred")
        self.assertIsNone(t.search(999))
        self.assertTrue(t.remove(100))
        self.assertFalse(t.remove(100))
        self.assertEqual(len(t), 0)

if __name__ == "__main__":
    unittest.main()
