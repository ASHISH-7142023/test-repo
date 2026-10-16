"""Doubly linked list with O(1) push, append, pop, and popleft operations."""

from typing import Any, List, Optional


class Node:
    def __init__(self, val: Any):
        self.val = val
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class DoublyLinkedList:
    """Two-way doubly linked list container."""

    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size = 0

    def append(self, val: Any) -> None:
        """Insert value at tail of list."""
        node = Node(val)
        if not self.tail:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self._size += 1

    def appendleft(self, val: Any) -> None:
        """Insert value at head of list."""
        node = Node(val)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._size += 1

    def pop(self) -> Any:
        """Remove and return element from tail."""
        if not self.tail:
            raise IndexError("pop from empty DoublyLinkedList")
        val = self.tail.val
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._size -= 1
        return val

    def popleft(self) -> Any:
        """Remove and return element from head."""
        if not self.head:
            raise IndexError("popleft from empty DoublyLinkedList")
        val = self.head.val
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self._size -= 1
        return val

    def to_list(self) -> List[Any]:
        """Convert elements to standard Python list."""
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

    def __len__(self) -> int:
        return self._size
