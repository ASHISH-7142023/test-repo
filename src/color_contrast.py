"""WCAG color contrast ratio calculations and accessibility compliance audits."""

from src.color_utils import hex_to_rgb


def relative_luminance(r: int, g: int, b: int) -> float:
    """Calculate relative luminance for sRGB color according to WCAG 2.1 specs."""
    def channel_lum(val: int) -> float:
        c = val / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    return 0.2126 * channel_lum(r) + 0.7152 * channel_lum(g) + 0.0722 * channel_lum(b)


def contrast_ratio(hex1: str, hex2: str) -> float:
    """Compute contrast ratio (1.0 to 21.0) between two hex colors."""
    r1, g1, b1 = hex_to_rgb(hex1)
    r2, g2, b2 = hex_to_rgb(hex2)
    l1 = relative_luminance(r1, g1, b1)
    l2 = relative_luminance(r2, g2, b2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return round((lighter + 0.05) / (darker + 0.05), 2)


def is_wcag_aa(hex_fg: str, hex_bg: str, large_text: bool = False) -> bool:
    """Check if color combination passes WCAG AA standard (4.5:1 normal, 3.0:1 large)."""
    ratio = contrast_ratio(hex_fg, hex_bg)
    return ratio >= (3.0 if large_text else 4.5)


def is_wcag_aaa(hex_fg: str, hex_bg: str, large_text: bool = False) -> bool:
    """Check if color combination passes WCAG AAA standard (7.0:1 normal, 4.5:1 large)."""
    ratio = contrast_ratio(hex_fg, hex_bg)
    return ratio >= (4.5 if large_text else 7.0)
