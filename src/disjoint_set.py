"""Disjoint-Set Union (Union-Find) with path compression and union-by-rank."""

from typing import Any, Dict


class DisjointSet:
    """Disjoint Set Union (DSU) data structure for connected components."""

    def __init__(self):
        self.parent: Dict[Any, Any] = {}
        self.rank: Dict[Any, int] = {}

    def make_set(self, x: Any) -> None:
        """Create new set containing element x."""
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x: Any) -> Any:
        """Find root representative of element x with path compression."""
        if x not in self.parent:
            self.make_set(x)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: Any, y: Any) -> bool:
        """Merge sets containing x and y. Returns True if sets were distinct."""
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

    def connected(self, x: Any, y: Any) -> bool:
        """Check if elements x and y share the same root."""
        return self.find(x) == self.find(y)
