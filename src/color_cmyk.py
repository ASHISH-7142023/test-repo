"""RGB and CMYK color space conversion utilities."""

from typing import Tuple


def rgb_to_cmyk(r: int, g: int, b: int) -> Tuple[float, float, float, float]:
    """Convert RGB [0..255] to CMYK percentages [0..100]."""
    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        raise ValueError("RGB values must be integers between 0 and 255.")

    if r == 0 and g == 0 and b == 0:
        return 0.0, 0.0, 0.0, 100.0

    r_p = r / 255.0
    g_p = g / 255.0
    b_p = b / 255.0

    k = 1.0 - max(r_p, g_p, b_p)
    c = (1.0 - r_p - k) / (1.0 - k)
    m = (1.0 - g_p - k) / (1.0 - k)
    y = (1.0 - b_p - k) / (1.0 - k)

    return round(c * 100, 2), round(m * 100, 2), round(y * 100, 2), round(k * 100, 2)


def cmyk_to_rgb(c: float, m: float, y: float, k: float) -> Tuple[int, int, int]:
    """Convert CMYK percentages [0..100] to RGB [0..255]."""
    c_p = c / 100.0
    m_p = m / 100.0
    y_p = y / 100.0
    k_p = k / 100.0

    r = round(255 * (1.0 - c_p) * (1.0 - k_p))
    g = round(255 * (1.0 - m_p) * (1.0 - k_p))
    b = round(255 * (1.0 - y_p) * (1.0 - k_p))

    return max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b))
