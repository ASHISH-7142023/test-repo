"""Roman numeral conversion and validation utilities."""

import re

ROMAN_MAP = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]

ROMAN_REGEX = re.compile(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")


def to_roman(n: int) -> str:
    """Convert integer (1 to 3999) to Roman numeral string."""
    if not isinstance(n, int) or not (1 <= n <= 3999):
        raise ValueError("Number must be an integer between 1 and 3999.")
    result = []
    for val, numeral in ROMAN_MAP:
        while n >= val:
            result.append(numeral)
            n -= val
    return "".join(result)


def from_roman(s: str) -> int:
    """Convert valid Roman numeral string to integer."""
    s = s.strip().upper()
    if not s or not ROMAN_REGEX.match(s):
        raise ValueError(f"Invalid Roman numeral: {s}")

    val_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev_val = 0

    for ch in reversed(s):
        curr_val = val_map[ch]
        if curr_val < prev_val:
            total -= curr_val
        else:
            total += curr_val
        prev_val = curr_val

    return total
