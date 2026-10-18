"""Kahn's algorithm for topological sorting and cycle detection in directed graphs."""

from collections import deque
from typing import Dict, List, Set, Tuple


def kahns_topological_sort(edges: List[Tuple[str, str]]) -> Tuple[List[str], bool]:
    """Perform topological sort using in-degree reduction."""
    nodes: Set[str] = set()
    adj: Dict[str, List[str]] = {}
    in_degree: Dict[str, int] = {}

    for u, v in edges:
        nodes.add(u)
        nodes.add(v)
        if u not in adj:
            adj[u] = []
        adj[u].append(v)
        in_degree[v] = in_degree.get(v, 0) + 1
        if u not in in_degree:
            in_degree[u] = 0

    queue = deque([node for node in nodes if in_degree.get(node, 0) == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in adj.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    has_cycle = len(order) < len(nodes)
    return order, has_cycle
