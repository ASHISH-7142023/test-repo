"""Graph algorithms: Topological sorting (Kahn's), cycle detection, and BFS shortest path."""

from collections import deque, defaultdict
from typing import Any, Dict, List, Optional


class Graph:
    """Graph structure with adjacency lists supporting directed and undirected graphs."""

    def __init__(self, directed: bool = True):
        self.directed = directed
        self.adj: Dict[Any, List[Any]] = defaultdict(list)

    def add_edge(self, u: Any, v: Any) -> None:
        """Add directed or undirected edge between u and v."""
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def topological_sort(self) -> List[Any]:
        """Kahn's algorithm for topological sorting of Directed Acyclic Graph (DAG)."""
        if not self.directed:
            raise ValueError("Topological sort is only valid for directed graphs.")

        in_degree: Dict[Any, int] = defaultdict(int)
        all_nodes = set(self.adj.keys())
        for neighbors in self.adj.values():
            for v in neighbors:
                all_nodes.add(v)
                in_degree[v] += 1

        queue = deque([n for n in all_nodes if in_degree[n] == 0])
        sorted_nodes = []

        while queue:
            node = queue.popleft()
            sorted_nodes.append(node)
            for neighbor in self.adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(sorted_nodes) != len(all_nodes):
            raise ValueError("Graph contains cycles; topological ordering impossible.")
        return sorted_nodes

    def shortest_path_bfs(self, start: Any, target: Any) -> Optional[List[Any]]:
        """Find unweighted shortest path from start to target using BFS."""
        if start == target:
            return [start]
        visited = {start}
        queue = deque([(start, [start])])

        while queue:
            curr, path = queue.popleft()
            for neighbor in self.adj[curr]:
                if neighbor == target:
                    return path + [target]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None
