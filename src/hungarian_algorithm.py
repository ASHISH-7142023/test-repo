"""
Kuhn-Munkres (Hungarian) Algorithm for Bipartite Minimum Weight Matching.
Solves the optimal linear sum assignment problem in O(N^3).
"""
from typing import List, Tuple

def hungarian_min_assignment(cost_matrix: List[List[float]]) -> Tuple[float, List[Tuple[int, int]]]:
    """
    Solves minimum cost assignment for an N x M matrix (N <= M).
    Returns: (min_total_cost, [(row, col), ...])
    """
    n = len(cost_matrix)
    if n == 0:
        return 0.0, []
    m = len(cost_matrix[0])
    if n > m:
        raise ValueError("Cost matrix must have at least as many columns as rows")

    u = [0.0] * (n + 1)
    v = [0.0] * (m + 1)
    p = [0] * (m + 1)
    way = [0] * (m + 1)

    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minv = [float("inf")] * (m + 1)
        used = [False] * (m + 1)
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = float("inf")
            j1 = 0
            for j in range(1, m + 1):
                if not used[j]:
                    cur = cost_matrix[i0 - 1][j - 1] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
            for j in range(0, m + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break

    assignment = []
    total_cost = 0.0
    for j in range(1, m + 1):
        if p[j] > 0:
            row = p[j] - 1
            col = j - 1
            assignment.append((row, col))
            total_cost += cost_matrix[row][col]

    assignment.sort(key=lambda x: x[0])
    return total_cost, assignment
