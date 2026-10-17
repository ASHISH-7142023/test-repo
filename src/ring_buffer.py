"""Circular buffer (ring buffer) implementation with configurable overwrite policy."""

from typing import Generic, TypeVar, Iterator, List, Optional

T = TypeVar("T")


class CircularBuffer(Generic[T]):
    """Fixed-capacity circular buffer with O(1) append, popleft, and peek."""

    def __init__(self, capacity: int, overwrite: bool = True) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self.capacity: int = capacity
        self.overwrite: bool = overwrite
        self._buffer: List[Optional[T]] = [None] * capacity
        self._head: int = 0
        self._tail: int = 0
        self._size: int = 0

    def append(self, item: T) -> None:
        """Add an item to the end of the buffer."""
        if self._size == self.capacity:
            if not self.overwrite:
                raise OverflowError("CircularBuffer is full and overwrite is disabled.")
            self._buffer[self._tail] = item
            self._tail = (self._tail + 1) % self.capacity
            self._head = (self._head + 1) % self.capacity
        else:
            self._buffer[self._tail] = item
            self._tail = (self._tail + 1) % self.capacity
            self._size += 1

    def popleft(self) -> T:
        """Remove and return the oldest item in the buffer."""
        if self._size == 0:
            raise IndexError("popleft from an empty CircularBuffer")
        item = self._buffer[self._head]
        self._buffer[self._head] = None
        self._head = (self._head + 1) % self.capacity
        self._size -= 1
        return item  # type: ignore

    def peek(self) -> T:
        """Return the oldest item without removing it."""
        if self._size == 0:
            raise IndexError("peek from an empty CircularBuffer")
        return self._buffer[self._head]  # type: ignore

    def is_full(self) -> bool:
        """Return True if buffer is at maximum capacity."""
        return self._size == self.capacity

    def is_empty(self) -> bool:
        """Return True if buffer has zero items."""
        return self._size == 0

    def clear(self) -> None:
        """Clear all items from the buffer."""
        self._buffer = [None] * self.capacity
        self._head = 0
        self._tail = 0
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[T]:
        for i in range(self._size):
            yield self._buffer[(self._head + i) % self.capacity]  # type: ignore

    def to_list(self) -> List[T]:
        """Convert elements to a standard Python list in FIFO order."""
        return list(self)
