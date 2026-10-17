"""Dijkstra's shortest path algorithm for weighted directed/undirected graphs."""

import heapq
from typing import Dict, List, Optional, Tuple


class WeightedGraph:
    """Adjacency list representation of a weighted graph."""

    def __init__(self):
        self.adj: Dict[str, List[Tuple[str, float]]] = {}

    def add_edge(self, u: str, v: str, weight: float, directed: bool = False) -> None:
        """Add a weighted edge between u and v."""
        if weight < 0:
            raise ValueError("Dijkstra does not support negative edge weights.")
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []

        self.adj[u].append((v, weight))
        if not directed:
            self.adj[v].append((u, weight))

    def dijkstra(self, start: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
        """Compute shortest distances and predecessors from start node."""
        distances: Dict[str, float] = {node: float("inf") for node in self.adj}
        predecessors: Dict[str, Optional[str]] = {node: None for node in self.adj}

        if start not in self.adj:
            return distances, predecessors

        distances[start] = 0.0
        pq: List[Tuple[float, str]] = [(0.0, start)]

        while pq:
            curr_dist, u = heapq.heappop(pq)

            if curr_dist > distances[u]:
                continue

            for v, weight in self.adj[u]:
                new_dist = curr_dist + weight
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    predecessors[v] = u
                    heapq.heappush(pq, (new_dist, v))

        return distances, predecessors

    def shortest_path(self, start: str, end: str) -> Tuple[List[str], float]:
        """Find the shortest path and its total cost from start to end."""
        distances, predecessors = self.dijkstra(start)
        if end not in distances or distances[end] == float("inf"):
            return [], float("inf")

        path = []
        curr: Optional[str] = end
        while curr is not None:
            path.append(curr)
            curr = predecessors[curr]
        path.reverse()
        return path, distances[end]
