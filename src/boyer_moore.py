"""Boyer-Moore string pattern matching algorithm using the Bad Character rule."""

from typing import Dict, List


def build_bad_char_table(pattern: str) -> Dict[str, int]:
    """Build bad character skip table mapping each character to its last index."""
    table: Dict[str, int] = {}
    for i, char in enumerate(pattern):
        table[char] = i
    return table


def boyer_moore_search(text: str, pattern: str) -> List[int]:
    """Search for pattern in text using Boyer-Moore bad character heuristic."""
    if not pattern:
        return []
    n = len(text)
    m = len(pattern)
    if m > n:
        return []

    bad_char = build_bad_char_table(pattern)
    occurrences = []
    shift = 0

    while shift <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            occurrences.append(shift)
            shift += (m - bad_char.get(text[shift + m], -1)) if shift + m < n else 1
        else:
            last_pos = bad_char.get(text[shift + j], -1)
            shift += max(1, j - last_pos)

    return occurrences


def boyer_moore_contains(text: str, pattern: str) -> bool:
    """Return True if pattern exists in text."""
    if not pattern:
        return True
    return len(boyer_moore_search(text, pattern)) > 0
