import unittest
from src.skip_list import SkipList

class TestSkipList(unittest.TestCase):
    def test_insert_and_contains(self):
        sl = SkipList()
        for x in [3, 1, 9, 5, 7]:
            sl.insert(x)
        self.assertEqual(len(sl), 5)
        self.assertTrue(sl.contains(1))
        self.assertTrue(sl.contains(7))
        self.assertFalse(sl.contains(4))
        self.assertFalse(sl.contains(10))

    def test_sorted_order(self):
        sl = SkipList()
        vals = [42, 10, 50, 20, 30]
        for v in vals:
            sl.insert(v)
        self.assertEqual(sl.to_list(), [10, 20, 30, 42, 50])

    def test_remove(self):
        sl = SkipList()
        sl.insert(100)
        sl.insert(200)
        self.assertTrue(sl.remove(100))
        self.assertFalse(sl.remove(999))
        self.assertEqual(len(sl), 1)
        self.assertFalse(sl.contains(100))
        self.assertTrue(sl.contains(200))

if __name__ == "__main__":
    unittest.main()
