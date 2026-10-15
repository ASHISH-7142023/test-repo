"""Hierarchical tree data structure with BFS and DFS traversal algorithms."""

from collections import deque
from typing import Any, Callable, List, Optional


class TreeNode:
    """Generic tree node supporting arbitrary payload and child nodes."""

    def __init__(self, val: Any, children: Optional[List["TreeNode"]] = None):
        self.val = val
        self.children: List["TreeNode"] = children if children is not None else []

    def add_child(self, child: "TreeNode") -> "TreeNode":
        self.children.append(child)
        return child


def dfs_traverse(root: Optional[TreeNode]) -> List[Any]:
    """Depth-First Search (pre-order) traversal returning node values."""
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        for child in reversed(node.children):
            stack.append(child)
    return result


def bfs_traverse(root: Optional[TreeNode]) -> List[Any]:
    """Breadth-First Search (level-order) traversal returning node values."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        for child in node.children:
            queue.append(child)
    return result


def find_node(root: Optional[TreeNode], predicate: Callable[[Any], bool]) -> Optional[TreeNode]:
    """Find first node whose value matches predicate."""
    if not root:
        return None
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if predicate(node.val):
            return node
        for child in node.children:
            queue.append(child)
    return None
