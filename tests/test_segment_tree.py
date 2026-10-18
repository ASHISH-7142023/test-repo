import unittest
from src.segment_tree import SegmentTree

class TestSegmentTree(unittest.TestCase):
    def test_range_minimum_query(self):
        st = SegmentTree([5, 2, 9, 1, 7], op=min, default=float("inf"))
        self.assertEqual(st.query(0, 2), 2)
        self.assertEqual(st.query(2, 4), 1)

    def test_update(self):
        st = SegmentTree([1, 3, 5, 7], op=lambda a, b: a + b, default=0)
        self.assertEqual(st.query(1, 3), 15)
        st.update(2, 10)
        self.assertEqual(st.query(1, 3), 20)

if __name__ == "__main__":
    unittest.main()
