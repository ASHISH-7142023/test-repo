"""
Hilbert Space-Filling Curve.
Maps 2D coordinates (x, y) to 1D index and vice versa, preserving 2D spatial locality.
"""
from typing import Tuple

def point_to_hilbert(x: int, y: int, order: int) -> int:
    """
    Maps 2D integer coordinates (x, y) to a 1D Hilbert curve distance d.
    order: bit order where grid size is 2^order.
    """
    if order <= 0:
        raise ValueError("order must be >= 1")
    n = 1 << order
    if not (0 <= x < n and 0 <= y < n):
        raise ValueError(f"Coordinates ({x}, {y}) out of bounds for order {order}")

    d = 0
    s = n // 2
    while s > 0:
        rx = 1 if (x & s) > 0 else 0
        ry = 1 if (y & s) > 0 else 0
        d += s * s * ((3 * rx) ^ ry)
        if ry == 0:
            if rx == 1:
                x = s - 1 - x
                y = s - 1 - y
            x, y = y, x
        s //= 2
    return d

def hilbert_to_point(d: int, order: int) -> Tuple[int, int]:
    """
    Maps a 1D Hilbert curve distance d to 2D integer coordinates (x, y).
    """
    if order <= 0:
        raise ValueError("order must be >= 1")
    n = 1 << order
    max_d = n * n
    if not (0 <= d < max_d):
        raise ValueError(f"Distance {d} out of range for order {order}")

    x = y = 0
    t = d
    s = 1
    while s < n:
        rx = 1 & (t // 2)
        ry = 1 & (t ^ rx)
        if ry == 0:
            if rx == 1:
                x = s - 1 - x
                y = s - 1 - y
            x, y = y, x
        x += s * rx
        y += s * ry
        t //= 4
        s *= 2
    return x, y
