"""
Hopcroft-Karp Bipartite Matching Algorithm.
Computes maximum cardinality matching in bipartite graphs in O(E * sqrt(V)).
"""
from collections import deque
from typing import Any, List, Tuple, Dict

def hopcroft_karp(
    u_nodes: List[Any],
    v_nodes: List[Any],
    edges: List[Tuple[Any, Any]]
) -> Tuple[int, Dict[Any, Any]]:
    """
    Finds the maximum cardinality matching between partition U and partition V.
    Returns: (matching_size, matching_map) where matching_map maps u <-> v.
    """
    adj: Dict[Any, List[Any]] = {u: [] for u in u_nodes}
    v_set = set(v_nodes)
    for u, v in edges:
        if u in adj and v in v_set:
            adj[u].append(v)

    pair_u: Dict[Any, Any] = {u: None for u in u_nodes}
    pair_v: Dict[Any, Any] = {v: None for v in v_nodes}
    dist: Dict[Any, int] = {}
    INF = float("inf")

    def bfs() -> bool:
        queue = deque()
        for u in u_nodes:
            if pair_u[u] is None:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[None] = INF

        while queue:
            u = queue.popleft()
            if dist[u] < dist[None]:
                for v in adj[u]:
                    next_u = pair_v[v]
                    if dist.get(next_u, INF) == INF:
                        dist[next_u] = dist[u] + 1
                        queue.append(next_u)
        return dist[None] != INF

    def dfs(u: Any) -> bool:
        if u is not None:
            for v in adj[u]:
                next_u = pair_v[v]
                if dist.get(next_u, INF) == dist[u] + 1:
                    if dfs(next_u):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    matching_size = 0
    while bfs():
        for u in u_nodes:
            if pair_u[u] is None and dfs(u):
                matching_size += 1

    matching: Dict[Any, Any] = {}
    for u, v in pair_u.items():
        if v is not None:
            matching[u] = v
            matching[v] = u

    return matching_size, matching
