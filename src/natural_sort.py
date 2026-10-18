"""Natural sort algorithm for human-friendly alphanumeric sorting."""

import re
from typing import Any, List, Union


def natural_sort_key(s: str) -> List[Union[int, str]]:
    """Convert string to list of integer and string chunks for natural comparison."""
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r"(\d+)", s)]


def natural_sort(strings: List[str]) -> List[str]:
    """Sort list of strings in human-friendly alphanumeric order."""
    return sorted(strings, key=natural_sort_key)
