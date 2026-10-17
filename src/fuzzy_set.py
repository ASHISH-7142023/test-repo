"""Fuzzy logic sets and membership functions."""

from typing import Callable


class TriangularMembership:
    """Triangular fuzzy membership function defined by points (a, b, c)."""

    def __init__(self, a: float, b: float, c: float):
        if not (a <= b <= c):
            raise ValueError("Triangular points must satisfy a <= b <= c.")
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x: float) -> float:
        if x <= self.a or x >= self.c:
            return 0.0
        if x == self.b:
            return 1.0
        if self.a < x < self.b:
            return (x - self.a) / (self.b - self.a)
        return (self.c - x) / (self.c - self.b)


class FuzzySet:
    """Fuzzy set with continuous membership function."""

    def __init__(self, membership_func: Callable[[float], float]):
        self.membership = membership_func

    def __call__(self, x: float) -> float:
        return max(0.0, min(1.0, self.membership(x)))

    def union(self, other: "FuzzySet") -> "FuzzySet":
        """Zadeh fuzzy OR (maximum)."""
        return FuzzySet(lambda x: max(self(x), other(x)))

    def intersection(self, other: "FuzzySet") -> "FuzzySet":
        """Zadeh fuzzy AND (minimum)."""
        return FuzzySet(lambda x: min(self(x), other(x)))

    def complement(self) -> "FuzzySet":
        """Zadeh fuzzy NOT (1 - mu)."""
        return FuzzySet(lambda x: 1.0 - self(x))
