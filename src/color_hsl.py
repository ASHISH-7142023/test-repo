"""RGB and HSL color space conversion utilities."""

from typing import Tuple


def rgb_to_hsl(r: int, g: int, b: int) -> Tuple[float, float, float]:
    """Convert RGB [0..255] to HSL (Hue: 0..360, Saturation: 0..100, Lightness: 0..100)."""
    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    cmax = max(r_norm, g_norm, b_norm)
    cmin = min(r_norm, g_norm, b_norm)
    delta = cmax - cmin

    l = (cmax + cmin) / 2.0

    if delta == 0:
        h = 0.0
        s = 0.0
    else:
        s = delta / (1.0 - abs(2.0 * l - 1.0))
        if cmax == r_norm:
            h = ((g_norm - b_norm) / delta) % 6.0
        elif cmax == g_norm:
            h = ((b_norm - r_norm) / delta) + 2.0
        else:
            h = ((r_norm - g_norm) / delta) + 4.0
        h *= 60.0

    return round(h, 2), round(s * 100.0, 2), round(l * 100.0, 2)


def hsl_to_rgb(h: float, s: float, l: float) -> Tuple[int, int, int]:
    """Convert HSL (H: 0..360, S: 0..100, L: 0..100) to RGB [0..255]."""
    s_norm = s / 100.0
    l_norm = l / 100.0

    c = (1.0 - abs(2.0 * l_norm - 1.0)) * s_norm
    x = c * (1.0 - abs((h / 60.0) % 2.0 - 1.0))
    m = l_norm - c / 2.0

    if 0 <= h < 60:
        r_p, g_p, b_p = c, x, 0
    elif 60 <= h < 120:
        r_p, g_p, b_p = x, c, 0
    elif 120 <= h < 180:
        r_p, g_p, b_p = 0, c, x
    elif 180 <= h < 240:
        r_p, g_p, b_p = 0, x, c
    elif 240 <= h < 300:
        r_p, g_p, b_p = x, 0, c
    else:
        r_p, g_p, b_p = c, 0, x

    r = round((r_p + m) * 255)
    g = round((g_p + m) * 255)
    b = round((b_p + m) * 255)
    return r, g, b


def hex_to_hsl(hex_str: str) -> Tuple[float, float, float]:
    """Convert hex color (#rgb or #rrggbb) to HSL."""
    h = hex_str.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r = int(h[0:2], 16)
    g = int(h[2:4], 16)
    b = int(h[4:6], 16)
    return rgb_to_hsl(r, g, b)


def hsl_to_hex(h: float, s: float, l: float) -> str:
    """Convert HSL to hex string #rrggbb."""
    r, g, b = hsl_to_rgb(h, s, l)
    return f"#{r:02x}{g:02x}{b:02x}"
