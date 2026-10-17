"""SkipList data structure providing O(log n) average time complexity."""

import random
from typing import Optional, List, Any


class SkipListNode:
    def __init__(self, val: Any, level: int):
        self.val = val
        self.forward: List[Optional["SkipListNode"]] = [None] * level


class SkipList:
    """Probabilistic alternative to balanced binary search trees."""

    def __init__(self, max_level: int = 16, p: float = 0.5):
        self.max_level = max_level
        self.p = p
        self.head = SkipListNode(float("-inf"), max_level)
        self.level = 1
        self._size = 0

    def _random_level(self) -> int:
        lvl = 1
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def insert(self, val: Any) -> None:
        update = [None] * self.max_level
        curr = self.head

        for i in reversed(range(self.level)):
            while curr.forward[i] and curr.forward[i].val < val:
                curr = curr.forward[i]
            update[i] = curr

        lvl = self._random_level()
        if lvl > self.level:
            for i in range(self.level, lvl):
                update[i] = self.head
            self.level = lvl

        new_node = SkipListNode(val, lvl)
        for i in range(lvl):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

        self._size += 1

    def contains(self, val: Any) -> bool:
        curr = self.head
        for i in reversed(range(self.level)):
            while curr.forward[i] and curr.forward[i].val < val:
                curr = curr.forward[i]
        curr = curr.forward[0]
        return curr is not None and curr.val == val

    def remove(self, val: Any) -> bool:
        update = [None] * self.max_level
        curr = self.head
        for i in reversed(range(self.level)):
            while curr.forward[i] and curr.forward[i].val < val:
                curr = curr.forward[i]
            update[i] = curr

        target = curr.forward[0]
        if target is None or target.val != val:
            return False

        for i in range(self.level):
            if update[i].forward[i] != target:
                break
            update[i].forward[i] = target.forward[i]

        while self.level > 1 and self.head.forward[self.level - 1] is None:
            self.level -= 1

        self._size -= 1
        return True

    def to_list(self) -> List[Any]:
        res = []
        curr = self.head.forward[0]
        while curr:
            res.append(curr.val)
            curr = curr.forward[0]
        return res

    def __len__(self) -> int:
        return self._size
