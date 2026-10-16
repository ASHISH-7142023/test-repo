"""Prefix tree (Trie) data structure for dictionary lookup and autocomplete."""

from typing import Dict, List, Optional


class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.is_terminal: bool = False


class Trie:
    """Trie structure storing strings with fast prefix search."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert word into Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_terminal = True

    def search(self, word: str) -> bool:
        """Check if exact word exists in Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_terminal

    def starts_with(self, prefix: str) -> bool:
        """Check if any inserted word starts with prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def autocomplete(self, prefix: str, limit: int = 10) -> List[str]:
        """Find all words matching given prefix up to limit."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        results: List[str] = []

        def dfs(curr: TrieNode, path: List[str]):
            if len(results) >= limit:
                return
            if curr.is_terminal:
                results.append("".join(path))
            for c, child in sorted(curr.children.items()):
                dfs(child, path + [c])

        dfs(node, list(prefix))
        return results
