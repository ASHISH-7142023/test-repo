"""Unit tests for PriorityQueue data structure."""

import unittest
from src.priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):

    def test_priority_order(self):
        pq = PriorityQueue()
        pq.push("low-priority", priority=10.0)
        pq.push("critical", priority=1.0)
        pq.push("medium", priority=5.0)

        self.assertEqual(pq.pop(), "critical")
        self.assertEqual(pq.pop(), "medium")
        self.assertEqual(pq.pop(), "low-priority")

    def test_empty_pop_raises(self):
        pq = PriorityQueue()
        with self.assertRaises(IndexError):
            pq.pop()


if __name__ == "__main__":
    unittest.main()
