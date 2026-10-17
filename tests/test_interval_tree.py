import unittest
from src.interval_tree import IntervalTree, Interval

class TestIntervalTree(unittest.TestCase):
    def test_overlap_queries(self):
        tree = IntervalTree()
        tree.insert(1, 5, "task-A")
        tree.insert(4, 8, "task-B")
        tree.insert(10, 15, "task-C")

        self.assertEqual(len(tree), 3)

        overlap_3_4 = tree.find_overlapping(3, 4)
        datas = {i.data for i in overlap_3_4}
        self.assertEqual(datas, {"task-A", "task-B"})

        at_point_12 = tree.find_at_point(12)
        self.assertEqual(len(at_point_12), 1)
        self.assertEqual(at_point_12[0].data, "task-C")

        at_point_9 = tree.find_at_point(9)
        self.assertEqual(len(at_point_9), 0)

    def test_invalid_interval(self):
        with self.assertRaises(ValueError):
            Interval(10, 5)

if __name__ == "__main__":
    unittest.main()
