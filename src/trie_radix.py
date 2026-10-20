"""
Radix Tree (Patricia Trie).
Compressed prefix tree merging common single-child edges for optimal string search.
"""
from typing import Optional, Dict, Any

class RadixNode:
    def __init__(self, prefix: str = "", is_terminal: bool = False, value: Any = None):
        self.prefix = prefix
        self.is_terminal = is_terminal
        self.value = value
        self.children: Dict[str, 'RadixNode'] = {}

class RadixTree:
    """Radix / Patricia Tree."""
    def __init__(self):
        self.root = RadixNode()
        self._count = 0

    def __len__(self) -> int:
        return self._count

    def insert(self, key: str, value: Any = True) -> None:
        curr = self.root
        i = 0
        while i < len(key):
            char = key[i]
            if char not in curr.children:
                curr.children[char] = RadixNode(prefix=key[i:], is_terminal=True, value=value)
                self._count += 1
                return

            child = curr.children[char]
            prefix = child.prefix
            common = 0
            while common < len(prefix) and i + common < len(key) and prefix[common] == key[i + common]:
                common += 1

            if common == len(prefix):
                i += common
                curr = child
            else:
                split = RadixNode(prefix=prefix[:common], is_terminal=False)
                child.prefix = prefix[common:]
                split.children[child.prefix[0]] = child
                curr.children[char] = split

                if i + common == len(key):
                    split.is_terminal = True
                    split.value = value
                    self._count += 1
                else:
                    new_child = RadixNode(prefix=key[i + common:], is_terminal=True, value=value)
                    split.children[new_child.prefix[0]] = new_child
                    self._count += 1
                return

        if not curr.is_terminal:
            curr.is_terminal = True
            curr.value = value
            self._count += 1
        else:
            curr.value = value

    def search(self, key: str) -> Optional[Any]:
        curr = self.root
        i = 0
        while i < len(key):
            char = key[i]
            if char not in curr.children:
                return None
            child = curr.children[char]
            prefix = child.prefix
            if not key[i:].startswith(prefix):
                return None
            i += len(prefix)
            curr = child
        return curr.value if curr.is_terminal else None
