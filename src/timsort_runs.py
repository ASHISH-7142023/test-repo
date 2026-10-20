"""
Timsort Run Detection and Natural Run Merge Utilities.
Detects ascending and strictly descending runs for hybrid sorting algorithms.
"""
from typing import List, Tuple

def find_natural_runs(seq: List[int]) -> List[Tuple[int, int, bool]]:
    """
    Scans sequence and identifies natural ascending and descending runs.
    Returns: list of (start_idx, end_idx_inclusive, is_descending).
    """
    n = len(seq)
    if n == 0:
        return []
    runs = []
    start = 0
    while start < n:
        if start == n - 1:
            runs.append((start, start, False))
            break
        if seq[start + 1] < seq[start]:
            end = start + 1
            while end + 1 < n and seq[end + 1] < seq[end]:
                end += 1
            runs.append((start, end, True))
            start = end + 1
        else:
            end = start + 1
            while end + 1 < n and seq[end + 1] >= seq[end]:
                end += 1
            runs.append((start, end, False))
            start = end + 1
    return runs

def reverse_run_slice(seq: List[int], start: int, end: int) -> None:
    """Reverse a descending run in-place to make it ascending."""
    i, j = start, end
    while i < j:
        seq[i], seq[j] = seq[j], seq[i]
        i += 1
        j -= 1
