"""Tarjan's strongly connected components (SCC) algorithm for directed graphs."""

from typing import Dict, List, Set


class TarjanSCC:
    """Finds all strongly connected components in a directed graph."""

    def __init__(self):
        self.adj: Dict[str, List[str]] = {}

    def add_edge(self, u: str, v: str) -> None:
        """Add directed edge from u to v."""
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append(v)

    def find_sccs(self) -> List[List[str]]:
        """Compute and return list of SCCs."""
        index = 0
        indices: Dict[str, int] = {}
        lowlinks: Dict[str, int] = {}
        on_stack: Set[str] = set()
        stack: List[str] = []
        sccs: List[List[str]] = []

        def strongconnect(node: str):
            nonlocal index
            indices[node] = index
            lowlinks[node] = index
            index += 1
            stack.append(node)
            on_stack.add(node)

            for neighbor in self.adj.get(node, []):
                if neighbor not in indices:
                    strongconnect(neighbor)
                    lowlinks[node] = min(lowlinks[node], lowlinks[neighbor])
                elif neighbor in on_stack:
                    lowlinks[node] = min(lowlinks[node], indices[neighbor])

            if lowlinks[node] == indices[node]:
                current_scc = []
                while True:
                    w = stack.pop()
                    on_stack.remove(w)
                    current_scc.append(w)
                    if w == node:
                        break
                sccs.append(sorted(current_scc))

        for node in sorted(self.adj.keys()):
            if node not in indices:
                strongconnect(node)

        return sccs
