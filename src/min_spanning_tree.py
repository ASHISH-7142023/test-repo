"""
Minimum Spanning Tree (MST) Algorithms: Kruskal and Prim.
"""
from typing import Any, List, Tuple, Dict
from heapq import heappush, heappop
from src.disjoint_set import DisjointSet

def kruskal_mst(
    vertices: List[Any],
    edges: List[Tuple[Any, Any, float]]
) -> Tuple[float, List[Tuple[Any, Any, float]]]:
    """
    Computes MST using Kruskal's algorithm with Disjoint Set Union.
    Returns: (total_weight, mst_edges)
    """
    dsu = DisjointSet()
    for v in vertices:
        dsu.find(v)

    sorted_edges = sorted(edges, key=lambda e: e[2])
    mst_edges = []
    total_weight = 0.0

    for u, v, w in sorted_edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, w))
            total_weight += w
            if len(mst_edges) == len(vertices) - 1:
                break

    return total_weight, mst_edges

def prim_mst(
    vertices: List[Any],
    edges: List[Tuple[Any, Any, float]],
    start: Any = None
) -> Tuple[float, List[Tuple[Any, Any, float]]]:
    """
    Computes MST using Prim's algorithm with priority queue.
    Returns: (total_weight, mst_edges)
    """
    if not vertices:
        return 0.0, []

    adj: Dict[Any, List[Tuple[float, Any, Any]]] = {v: [] for v in vertices}
    for u, v, w in edges:
        adj[u].append((w, u, v))
        adj[v].append((w, v, u))

    start_v = start if start is not None and start in vertices else vertices[0]
    visited = {start_v}
    heap: List[Tuple[float, Any, Any]] = []
    for edge in adj[start_v]:
        heappush(heap, edge)

    mst_edges = []
    total_weight = 0.0

    while heap and len(visited) < len(vertices):
        w, u, v = heappop(heap)
        if v in visited:
            continue
        visited.add(v)
        mst_edges.append((u, v, w))
        total_weight += w
        for edge in adj[v]:
            if edge[2] not in visited:
                heappush(heap, edge)

    return total_weight, mst_edges
