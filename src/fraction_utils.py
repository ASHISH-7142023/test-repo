"""Rational fraction representation and continued fraction approximations."""

import math
from typing import List


class RationalFraction:
    """Exact rational fraction with numerator and denominator."""

    def __init__(self, num: int, den: int = 1):
        if den == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if den < 0:
            num = -num
            den = -den
        common = math.gcd(abs(num), den)
        self.num = num // common
        self.den = den // common

    def __add__(self, other: "RationalFraction") -> "RationalFraction":
        return RationalFraction(self.num * other.den + other.num * self.den, self.den * other.den)

    def __sub__(self, other: "RationalFraction") -> "RationalFraction":
        return RationalFraction(self.num * other.den - other.num * self.den, self.den * other.den)

    def __mul__(self, other: "RationalFraction") -> "RationalFraction":
        return RationalFraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other: "RationalFraction") -> "RationalFraction":
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction.")
        return RationalFraction(self.num * other.den, self.den * other.num)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, RationalFraction):
            return False
        return self.num == other.num and self.den == other.den

    def __float__(self) -> float:
        return self.num / self.den

    def __repr__(self) -> str:
        return f"{self.num}/{self.den}" if self.den != 1 else str(self.num)

    def to_continued_fraction(self) -> List[int]:
        """Convert fraction to continued fraction list of coefficients [a0; a1, a2, ...]."""
        coeffs = []
        n, d = self.num, self.den
        while d != 0:
            q = n // d
            coeffs.append(q)
            n, d = d, n - q * d
        return coeffs


def approximate_float(val: float, max_denominator: int = 1000) -> RationalFraction:
    """Find the best rational approximation p/q for a float such that q <= max_denominator."""
    p0, q0 = 0, 1
    p1, q1 = 1, 0
    x = val

    while True:
        a = math.floor(x)
        p2 = a * p1 + p0
        q2 = a * q1 + q0

        if q2 > max_denominator:
            break

        p0, q0 = p1, q1
        p1, q1 = p2, q2

        frac = x - a
        if abs(frac) < 1e-12:
            break
        x = 1.0 / frac

    return RationalFraction(p1, q1)
