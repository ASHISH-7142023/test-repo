"""A* (A-Star) 2D Grid Pathfinding with Manhattan & Euclidean heuristics."""

import heapq
import math
from typing import Dict, List, Optional, Tuple

Coord = Tuple[int, int]


def manhattan_distance(a: Coord, b: Coord) -> float:
    return float(abs(a[0] - b[0]) + abs(a[1] - b[1]))


def euclidean_distance(a: Coord, b: Coord) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def astar_grid(
    grid: List[List[int]],
    start: Coord,
    goal: Coord,
    allow_diagonal: bool = False,
) -> Tuple[List[Coord], float]:
    """Find the shortest path from start to goal in a grid (0 = open, 1 = obstacle)."""
    rows = len(grid)
    if rows == 0:
        return [], float("inf")
    cols = len(grid[0])

    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        raise ValueError("Start is outside grid bounds.")
    if not (0 <= goal[0] < rows and 0 <= goal[1] < cols):
        raise ValueError("Goal is outside grid bounds.")
    if grid[start[0]][start[1]] != 0 or grid[goal[0]][goal[1]] != 0:
        return [], float("inf")

    dirs = [(-1, 0, 1.0), (1, 0, 1.0), (0, -1, 1.0), (0, 1, 1.0)]
    if allow_diagonal:
        diag_cost = math.sqrt(2)
        dirs += [(-1, -1, diag_cost), (-1, 1, diag_cost), (1, -1, diag_cost), (1, 1, diag_cost)]

    h_fn = euclidean_distance if allow_diagonal else manhattan_distance

    pq: List[Tuple[float, float, Coord]] = [(h_fn(start, goal), 0.0, start)]
    g_scores: Dict[Coord, float] = {start: 0.0}
    parents: Dict[Coord, Optional[Coord]] = {start: None}

    while pq:
        f, g, curr = heapq.heappop(pq)

        if curr == goal:
            path = []
            c: Optional[Coord] = curr
            while c is not None:
                path.append(c)
                c = parents[c]
            path.reverse()
            return path, g

        if g > g_scores.get(curr, float("inf")):
            continue

        for dr, dc, cost in dirs:
            nr, nc = curr[0] + dr, curr[1] + dc
            neighbor = (nr, nc)
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                tentative_g = g + cost
                if tentative_g < g_scores.get(neighbor, float("inf")):
                    g_scores[neighbor] = tentative_g
                    parents[neighbor] = curr
                    f_score = tentative_g + h_fn(neighbor, goal)
                    heapq.heappush(pq, (f_score, tentative_g, neighbor))

    return [], float("inf")
