"""2D matrix manipulation, transpose, rotation, and linear transformations."""

from typing import List, TypeVar

T = TypeVar("T")


def transpose(matrix: List[List[T]]) -> List[List[T]]:
    """Transpose a 2D matrix (swap rows with columns)."""
    if not matrix or not matrix[0]:
        return []
    return [list(row) for row in zip(*matrix)]


def rotate_90_clockwise(matrix: List[List[T]]) -> List[List[T]]:
    """Rotate a square or rectangular 2D matrix 90 degrees clockwise."""
    if not matrix or not matrix[0]:
        return []
    return [list(reversed(col)) for col in zip(*matrix)]


def identity_matrix(n: int) -> List[List[int]]:
    """Generate an n x n identity matrix."""
    if n <= 0:
        return []
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def matrix_multiply(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
    """Multiply two 2D numeric matrices."""
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("Incompatible matrix dimensions for multiplication.")
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    result = [[0.0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = sum(a[i][k] * b[k][j] for k in range(cols_a))
    return result
