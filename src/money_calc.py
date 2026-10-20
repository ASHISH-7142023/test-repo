"""
Arbitrary-Precision Financial Currency Arithmetic & Splitting.
Avoids floating-point drift with fixed-point integers and fair cent allocations.
"""
from typing import List

class Money:
    """Represents monetary amount in integer base units (e.g. cents)."""
    def __init__(self, amount_units: int, currency: str = "USD"):
        self.units = int(amount_units)
        self.currency = currency.upper()

    @classmethod
    def from_float(cls, amount: float, currency: str = "USD", decimals: int = 2) -> 'Money':
        units = round(amount * (10 ** decimals))
        return cls(units, currency)

    @property
    def amount(self) -> float:
        return self.units / 100.0

    def __repr__(self) -> str:
        return f"{self.currency} {self.amount:.2f}"

    def __add__(self, other: 'Money') -> 'Money':
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.units + other.units, self.currency)

    def __sub__(self, other: 'Money') -> 'Money':
        if self.currency != other.currency:
            raise ValueError("Cannot subtract different currencies")
        return Money(self.units - other.units, self.currency)

    def split(self, n: int) -> List['Money']:
        """Fairly splits the money into n parts, allocating remainder cents to the first parts."""
        if n <= 0:
            raise ValueError("Split parts must be positive")
        base = self.units // n
        rem = self.units % n
        parts = []
        for i in range(n):
            extra = 1 if i < rem else 0
            parts.append(Money(base + extra, self.currency))
        return parts
