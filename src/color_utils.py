"""ANSI terminal color, styling, and text decoration utilities."""

import re
from typing import Tuple

# Regex to strip ANSI escape sequences
_ANSI_ESCAPE_PATTERN = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

# Standard ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

# Standard foreground colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright foreground colors
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"


def colorize(text: str, color_code: str) -> str:
    """Wrap text in an ANSI color code and reset afterward."""
    return f"{color_code}{text}{RESET}"


def rgb(text: str, r: int, g: int, b: int) -> str:
    """Format text with 24-bit TrueColor RGB foreground."""
    return f"\033[38;2;{r};{g};{b}m{text}{RESET}"


def hex_to_rgb(hex_code: str) -> Tuple[int, int, int]:
    """Convert hex color string (e.g. '#3498db' or '3498db') to (R, G, B) tuple."""
    clean_hex = hex_code.lstrip("#")
    if len(clean_hex) == 3:
        clean_hex = "".join(c * 2 for c in clean_hex)
    if len(clean_hex) != 6:
        raise ValueError(f"Invalid hex color code: '{hex_code}'")
    return int(clean_hex[0:2], 16), int(clean_hex[2:4], 16), int(clean_hex[4:6], 16)


def hex_color(text: str, hex_code: str) -> str:
    """Format text with 24-bit TrueColor specified by hex color string."""
    r, g, b = hex_to_rgb(hex_code)
    return rgb(text, r, g, b)


def strip_ansi(text: str) -> str:
    """Remove all ANSI color and escape sequences from text."""
    if not text:
        return ""
    return _ANSI_ESCAPE_PATTERN.sub("", text)
