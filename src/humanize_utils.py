"""Human-friendly data representations: ordinals, natural lists, and formatted integers."""

from typing import List, Union


def ordinal(n: int) -> str:
    """Format an integer with its English ordinal suffix (1st, 2nd, 3rd, etc.)."""
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


def intcomma(val: Union[int, float]) -> str:
    """Format a number with comma thousands-separators (e.g. 1,000,000)."""
    if isinstance(val, int):
        return f"{val:,}"
    return f"{val:,.2f}"


def natural_list(items: List[str], conjunction: str = "and") -> str:
    """Format list of strings into Oxford-comma English sentence (e.g. 'A, B, and C')."""
    if not items:
        return ""
    if len(items) == 1:
        return str(items[0])
    if len(items) == 2:
        return f"{items[0]} {conjunction} {items[1]}"
    return f"{', '.join(items[:-1])}, {conjunction} {items[-1]}"
