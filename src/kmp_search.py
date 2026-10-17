"""Knuth-Morris-Pratt (KMP) string pattern matching algorithm."""

from typing import List


def compute_lps(pattern: str) -> List[int]:
    """Compute the Longest Proper Prefix which is also Suffix (LPS) array."""
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text: str, pattern: str) -> List[int]:
    """Search for all occurrences of pattern in text using KMP. Returns 0-based indices."""
    if not pattern:
        return []
    n = len(text)
    m = len(pattern)
    if m > n:
        return []

    lps = compute_lps(pattern)
    occurrences = []
    i = 0
    j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return occurrences


def kmp_contains(text: str, pattern: str) -> bool:
    """Return True if pattern exists in text."""
    if not pattern:
        return True
    return len(kmp_search(text, pattern)) > 0
