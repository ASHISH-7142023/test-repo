"""
Color Palette Generator & Harmony Calculator.
Generates complementary, triadic, analogous, and monochromatic palettes from RGB/Hex.
"""
from typing import List, Tuple
from src.color_hsl import rgb_to_hsl, hsl_to_rgb

def hex_to_rgb(hex_code: str) -> Tuple[int, int, int]:
    clean = hex_code.lstrip("#")
    if len(clean) == 3:
        clean = "".join(c * 2 for c in clean)
    if len(clean) != 6:
        raise ValueError("Invalid hex color code")
    return int(clean[0:2], 16), int(clean[2:4], 16), int(clean[4:6], 16)

def rgb_to_hex(r: int, g: int, b: int) -> str:
    return f"#{r:02x}{g:02x}{b:02x}"

def generate_complementary_palette(r: int, g: int, b: int) -> List[Tuple[int, int, int]]:
    """Returns base color and its 180-degree opposite."""
    h, s, l = rgb_to_hsl(r, g, b)
    comp_h = (h + 180) % 360
    return [(r, g, b), hsl_to_rgb(comp_h, s, l)]

def generate_triadic_palette(r: int, g: int, b: int) -> List[Tuple[int, int, int]]:
    """Returns base color and two 120-degree spaced colors."""
    h, s, l = rgb_to_hsl(r, g, b)
    h1 = (h + 120) % 360
    h2 = (h + 240) % 360
    return [(r, g, b), hsl_to_rgb(h1, s, l), hsl_to_rgb(h2, s, l)]

def generate_analogous_palette(r: int, g: int, b: int, angle: int = 30) -> List[Tuple[int, int, int]]:
    """Returns base color and two adjacent colors (+/- angle)."""
    h, s, l = rgb_to_hsl(r, g, b)
    h_prev = (h - angle) % 360
    h_next = (h + angle) % 360
    return [hsl_to_rgb(h_prev, s, l), (r, g, b), hsl_to_rgb(h_next, s, l)]

def generate_monochromatic_palette(r: int, g: int, b: int, steps: int = 5) -> List[Tuple[int, int, int]]:
    """Returns varying lightness shades of the base color."""
    h, s, _ = rgb_to_hsl(r, g, b)
    palette = []
    for i in range(1, steps + 1):
        lightness = int((i / (steps + 1)) * 100)
        palette.append(hsl_to_rgb(h, s, lightness))
    return palette
