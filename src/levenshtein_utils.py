"""Levenshtein edit distance and fuzzy string similarity ratio calculations."""

from typing import List, Optional, Tuple


def levenshtein_distance(s1: str, s2: str) -> int:
    """Calculate minimum single-character edits (insertions, deletions, substitutions)."""
    if s1 == s2:
        return 0
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)

    prev_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr_row = [i + 1] + [0] * len(s2)
        for j, c2 in enumerate(s2):
            insertions = prev_row[j + 1] + 1
            deletions = curr_row[j] + 1
            substitutions = prev_row[j] + (0 if c1 == c2 else 1)
            curr_row[j + 1] = min(insertions, deletions, substitutions)
        prev_row = curr_row

    return prev_row[-1]


def similarity_ratio(s1: str, s2: str) -> float:
    """Calculate normalized similarity ratio between 0.0 and 1.0."""
    max_len = max(len(s1), len(s2))
    if max_len == 0:
        return 1.0
    dist = levenshtein_distance(s1, s2)
    return round(1.0 - (dist / max_len), 4)


def find_closest_match(word: str, candidates: List[str]) -> Optional[str]:
    """Find candidate string with highest similarity ratio."""
    if not candidates:
        return None
    return max(candidates, key=lambda c: similarity_ratio(word, c))
