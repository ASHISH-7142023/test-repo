"""Compact bracket and dictionary serialization for n-ary tree structures."""

from typing import Dict, Any
from src.tree_utils import TreeNode


def serialize_to_brackets(root: TreeNode) -> str:
    """Serialize a tree into a bracketed string: val(child1,child2)."""
    if not root.children:
        return str(root.val)
    children_str = ",".join(serialize_to_brackets(c) for c in root.children)
    return f"{root.val}({children_str})"


def deserialize_from_brackets(expr: str) -> TreeNode:
    """Deserialize a bracketed string into a TreeNode tree."""
    expr = expr.strip()
    if not expr:
        raise ValueError("Cannot deserialize empty expression")

    idx = expr.find("(")
    if idx == -1:
        return TreeNode(expr)

    val = expr[:idx].strip()
    node = TreeNode(val)

    inner = expr[idx + 1 : -1].strip()
    if not inner:
        return node

    depth = 0
    start = 0
    for i, ch in enumerate(inner):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif ch == "," and depth == 0:
            node.add_child(deserialize_from_brackets(inner[start:i]))
            start = i + 1

    node.add_child(deserialize_from_brackets(inner[start:]))
    return node


def tree_to_dict(root: TreeNode) -> Dict[str, Any]:
    """Convert tree to a nested dictionary representation."""
    return {
        "val": root.val,
        "children": [tree_to_dict(c) for c in root.children],
    }


def dict_to_tree(d: Dict[str, Any]) -> TreeNode:
    """Reconstruct a TreeNode from a dictionary representation."""
    node = TreeNode(d["val"])
    for child_dict in d.get("children", []):
        node.add_child(dict_to_tree(child_dict))
    return node
