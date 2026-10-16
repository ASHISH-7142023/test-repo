"""Consistent Hashing ring with virtual node replicas for distributed sharding."""

import hashlib
import bisect
from typing import Any, Dict, List, Optional


class HashRing:
    """Consistent hash ring distributing keys across multiple target nodes."""

    def __init__(self, replicas: int = 100):
        self.replicas = replicas
        self.ring: List[int] = []
        self.ring_map: Dict[int, str] = {}
        self.nodes: set = set()

    def _hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode("utf-8")).hexdigest(), 16)

    def add_node(self, node: str) -> None:
        """Add server node with virtual replica hashes to ring."""
        self.nodes.add(node)
        for i in range(self.replicas):
            vnode_key = f"{node}#{i}"
            h = self._hash(vnode_key)
            idx = bisect.bisect_right(self.ring, h)
            self.ring.insert(idx, h)
            self.ring_map[h] = node

    def remove_node(self, node: str) -> None:
        """Remove server node and its virtual replicas from ring."""
        if node not in self.nodes:
            return
        self.nodes.remove(node)
        for i in range(self.replicas):
            vnode_key = f"{node}#{i}"
            h = self._hash(vnode_key)
            if h in self.ring_map:
                del self.ring_map[h]
                idx = bisect.bisect_left(self.ring, h)
                if idx < len(self.ring) and self.ring[idx] == h:
                    self.ring.pop(idx)

    def get_node(self, key: str) -> Optional[str]:
        """Find the designated node responsible for a given data key."""
        if not self.ring:
            return None
        h = self._hash(key)
        idx = bisect.bisect_right(self.ring, h)
        if idx == len(self.ring):
            idx = 0
        return self.ring_map[self.ring[idx]]
