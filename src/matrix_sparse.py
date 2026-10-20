"""
Compressed Dictionary of Keys (DOK) Sparse Matrix.
Memory-efficient representation of sparse 2D numeric matrices with basic operations.
"""
from typing import Dict, Tuple

class SparseMatrix:
    """Dictionary of Keys (DOK) Sparse Matrix."""
    def __init__(self, rows: int, cols: int):
        if rows <= 0 or cols <= 0:
            raise ValueError("Dimensions must be positive")
        self.rows = rows
        self.cols = cols
        self.data: Dict[Tuple[int, int], float] = {}

    def __getitem__(self, key: Tuple[int, int]) -> float:
        r, c = key
        if not (0 <= r < self.rows and 0 <= c < self.cols):
            raise IndexError("Index out of matrix bounds")
        return self.data.get((r, c), 0.0)

    def __setitem__(self, key: Tuple[int, int], value: float) -> None:
        r, c = key
        if not (0 <= r < self.rows and 0 <= c < self.cols):
            raise IndexError("Index out of matrix bounds")
        if abs(value) < 1e-12:
            self.data.pop((r, c), None)
        else:
            self.data[(r, c)] = float(value)

    @property
    def nnz(self) -> int:
        return len(self.data)

    @property
    def density(self) -> float:
        return self.nnz / (self.rows * self.cols)

    def add(self, other: 'SparseMatrix') -> 'SparseMatrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition")
        res = SparseMatrix(self.rows, self.cols)
        all_keys = set(self.data.keys()).union(other.data.keys())
        for k in all_keys:
            val = self.data.get(k, 0.0) + other.data.get(k, 0.0)
            if abs(val) >= 1e-12:
                res.data[k] = val
        return res

    def scalar_mul(self, scalar: float) -> 'SparseMatrix':
        res = SparseMatrix(self.rows, self.cols)
        if abs(scalar) < 1e-12:
            return res
        for k, v in self.data.items():
            res.data[k] = v * scalar
        return res

    def to_dense(self) -> list:
        dense = [[0.0] * self.cols for _ in range(self.rows)]
        for (r, c), val in self.data.items():
            dense[r][c] = val
        return dense
