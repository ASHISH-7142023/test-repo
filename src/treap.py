"""
Treap (Cartesian Tree / Tree-Heap).
Maintains binary search tree on keys and max-heap on random priorities.
"""
import random
from typing import Any, Optional, List, Tuple

class TreapNode:
    def __init__(self, key: Any, priority: Optional[float] = None, value: Any = None):
        self.key = key
        self.value = value if value is not None else key
        self.priority = priority if priority is not None else random.random()
        self.left: Optional['TreapNode'] = None
        self.right: Optional['TreapNode'] = None
        self.size: int = 1

    def update_size(self) -> None:
        self.size = 1 + (self.left.size if self.left else 0) + (self.right.size if self.right else 0)

class Treap:
    """
    Randomized balanced binary search tree (Treap).
    """
    def __init__(self):
        self.root: Optional[TreapNode] = None

    def _split(self, node: Optional[TreapNode], key: Any) -> Tuple[Optional[TreapNode], Optional[TreapNode]]:
        if not node:
            return None, None
        if node.key <= key:
            left, right = self._split(node.right, key)
            node.right = left
            node.update_size()
            return node, right
        else:
            left, right = self._split(node.left, key)
            node.left = right
            node.update_size()
            return left, node

    def _merge(self, left: Optional[TreapNode], right: Optional[TreapNode]) -> Optional[TreapNode]:
        if not left or not right:
            return left or right
        if left.priority > right.priority:
            left.right = self._merge(left.right, right)
            left.update_size()
            return left
        else:
            right.left = self._merge(left, right.left)
            right.update_size()
            return right

    def insert(self, key: Any, priority: Optional[float] = None, value: Any = None) -> None:
        node = TreapNode(key, priority, value)
        left, right = self._split(self.root, key)
        self.root = self._merge(self._merge(left, node), right)

    def search(self, key: Any) -> Optional[Any]:
        curr = self.root
        while curr:
            if curr.key == key:
                return curr.value
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def remove(self, key: Any) -> bool:
        if self.search(key) is None:
            return False
        left, right = self._split(self.root, key)
        def _remove_exact(n: Optional[TreapNode], k: Any) -> Optional[TreapNode]:
            if not n:
                return None
            if n.key == k:
                return self._merge(n.left, n.right)
            elif k < n.key:
                n.left = _remove_exact(n.left, k)
            else:
                n.right = _remove_exact(n.right, k)
            n.update_size()
            return n

        self.root = self._merge(_remove_exact(left, key), right)
        return True

    def inorder(self) -> List[Any]:
        res = []
        def _dfs(n: Optional[TreapNode]):
            if not n:
                return
            _dfs(n.left)
            res.append(n.key)
            _dfs(n.right)
        _dfs(self.root)
        return res

    def __len__(self) -> int:
        return self.root.size if self.root else 0

    def kth_smallest(self, k: int) -> Optional[Any]:
        """Return 1-indexed kth smallest key."""
        if k <= 0 or k > len(self):
            return None
        curr = self.root
        while curr:
            left_size = curr.left.size if curr.left else 0
            if left_size + 1 == k:
                return curr.key
            elif k <= left_size:
                curr = curr.left
            else:
                k -= left_size + 1
                curr = curr.right
        return None
