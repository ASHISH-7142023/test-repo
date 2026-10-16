"""Bitwise arithmetic, bitmask manipulation, and binary representation utilities."""


def count_set_bits(n: int) -> int:
    """Return count of 1s in integer binary representation (Hamming weight)."""
    return bin(n).count("1")


def is_power_of_two(n: int) -> bool:
    """Determine whether integer is a non-zero power of two."""
    return n > 0 and (n & (n - 1)) == 0


def get_bit(n: int, bit_index: int) -> int:
    """Retrieve the value of bit at index (0-indexed)."""
    return (n >> bit_index) & 1


def set_bit(n: int, bit_index: int) -> int:
    """Set bit at index to 1."""
    return n | (1 << bit_index)


def clear_bit(n: int, bit_index: int) -> int:
    """Clear bit at index to 0."""
    return n & ~(1 << bit_index)


def toggle_bit(n: int, bit_index: int) -> int:
    """Invert bit at index."""
    return n ^ (1 << bit_index)


def to_binary_string(n: int, width: int = 8) -> str:
    """Format integer as binary string padded with leading zeros."""
    return format(n, f"0{width}b")
