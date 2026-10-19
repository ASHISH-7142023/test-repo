"""
Bellman-Ford Shortest Path Algorithm.
Supports negative edge weights and negative cycle detection.
"""
from typing import Any, List, Tuple, Dict, Optional

def bellman_ford(
    vertices: List[Any],
    edges: List[Tuple[Any, Any, float]],
    source: Any
) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]], bool]:
    """
    Computes single-source shortest paths on graphs with arbitrary weights.
    Returns: (distances, predecessors, has_negative_cycle)
    """
    if source not in vertices:
        raise ValueError(f"Source {source} not in vertices")

    dist: Dict[Any, float] = {v: float("inf") for v in vertices}
    pred: Dict[Any, Optional[Any]] = {v: None for v in vertices}
    dist[source] = 0.0

    # Relax edges |V| - 1 times
    for _ in range(len(vertices) - 1):
        relaxed = False
        for u, v, weight in edges:
            if dist[u] != float("inf") and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                pred[v] = u
                relaxed = True
        if not relaxed:
            break

    # Check for negative-weight cycles
    has_negative_cycle = False
    for u, v, weight in edges:
        if dist[u] != float("inf") and dist[u] + weight < dist[v]:
            has_negative_cycle = True
            break

    return dist, pred, has_negative_cycle

def shortest_path_bf(
    vertices: List[Any],
    edges: List[Tuple[Any, Any, float]],
    source: Any,
    target: Any
) -> Tuple[Optional[List[Any]], float]:
    """
    Returns path and distance between source and target using Bellman-Ford.
    Raises ValueError if a negative cycle is detected.
    """
    dist, pred, has_cycle = bellman_ford(vertices, edges, source)
    if has_cycle:
        raise ValueError("Graph contains a negative weight cycle")
    if dist[target] == float("inf"):
        return None, float("inf")

    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = pred[curr]
    path.reverse()
    return path, dist[target]
