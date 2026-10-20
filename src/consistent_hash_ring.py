"""
Virtual-Node Consistent Hash Ring.
Distributes keys across multiple server nodes using SHA-256 and configurable virtual replicas.
"""
import hashlib
import bisect
from typing import List, Dict, Optional

class ConsistentHashRing:
    """Consistent Hash Ring with virtual nodes."""
    def __init__(self, nodes: Optional[List[str]] = None, replicas: int = 100):
        if replicas <= 0:
            raise ValueError("replicas must be > 0")
        self.replicas = replicas
        self.ring: List[int] = []
        self.vnode_to_node: Dict[int, str] = {}
        self.nodes: set = set()
        if nodes:
            for node in nodes:
                self.add_node(node)

    def _hash(self, key: str) -> int:
        return int(hashlib.sha256(key.encode("utf-8")).hexdigest()[:16], 16)

    def add_node(self, node: str) -> None:
        if node in self.nodes:
            return
        self.nodes.add(node)
        for i in range(self.replicas):
            vnode_key = f"{node}#vnode{i}"
            h = self._hash(vnode_key)
            bisect.insort(self.ring, h)
            self.vnode_to_node[h] = node

    def remove_node(self, node: str) -> bool:
        if node not in self.nodes:
            return False
        self.nodes.remove(node)
        for i in range(self.replicas):
            vnode_key = f"{node}#vnode{i}"
            h = self._hash(vnode_key)
            idx = bisect.bisect_left(self.ring, h)
            if idx < len(self.ring) and self.ring[idx] == h:
                self.ring.pop(idx)
                self.vnode_to_node.pop(h, None)
        return True

    def get_node(self, key: str) -> Optional[str]:
        if not self.ring:
            return None
        h = self._hash(key)
        idx = bisect.bisect_right(self.ring, h)
        if idx == len(self.ring):
            idx = 0
        return self.vnode_to_node[self.ring[idx]]
