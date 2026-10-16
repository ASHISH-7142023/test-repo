"""Unit tests for DoublyLinkedList data structure."""

import unittest
from src.linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def test_append_and_to_list(self):
        dll = DoublyLinkedList()
        dll.append(10)
        dll.append(20)
        dll.appendleft(5)
        self.assertEqual(dll.to_list(), [5, 10, 20])
        self.assertEqual(len(dll), 3)

    def test_pop_and_popleft(self):
        dll = DoublyLinkedList()
        dll.append("A")
        dll.append("B")
        dll.append("C")

        self.assertEqual(dll.pop(), "C")
        self.assertEqual(dll.popleft(), "A")
        self.assertEqual(dll.to_list(), ["B"])


if __name__ == "__main__":
    unittest.main()
