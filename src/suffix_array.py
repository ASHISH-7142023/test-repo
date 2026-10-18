"""Suffix Array construction and O(m log n) substring search."""

from typing import List, Optional


def build_suffix_array(text: str) -> List[int]:
    """Construct suffix array containing sorted suffix start indices."""
    suffixes = [(text[i:], i) for i in range(len(text))]
    suffixes.sort(key=lambda x: x[0])
    return [idx for _, idx in suffixes]


def suffix_array_search(text: str, pattern: str, sa: Optional[List[int]] = None) -> List[int]:
    """Search for all occurrences of pattern in text using suffix array and binary search."""
    if not pattern or not text:
        return []
    if sa is None:
        sa = build_suffix_array(text)

    n = len(text)
    m = len(pattern)

    low = 0
    high = n - 1
    left_idx = -1
    while low <= high:
        mid = (low + high) // 2
        suffix = text[sa[mid]: sa[mid] + m]
        if suffix >= pattern:
            if suffix == pattern:
                left_idx = mid
            high = mid - 1
        else:
            low = mid + 1

    if left_idx == -1:
        return []

    low = left_idx
    high = n - 1
    right_idx = left_idx
    while low <= high:
        mid = (low + high) // 2
        suffix = text[sa[mid]: sa[mid] + m]
        if suffix <= pattern:
            if suffix == pattern:
                right_idx = mid
            low = mid + 1
        else:
            high = mid - 1

    return sorted(sa[i] for i in range(left_idx, right_idx + 1))


def longest_repeated_substring(text: str) -> str:
    """Find the longest substring appearing at least twice in text."""
    if len(text) < 2:
        return ""
    sa = build_suffix_array(text)
    longest = ""
    for i in range(len(sa) - 1):
        s1 = text[sa[i]:]
        s2 = text[sa[i + 1]:]
        common_len = 0
        limit = min(len(s1), len(s2))
        while common_len < limit and s1[common_len] == s2[common_len]:
            common_len += 1
        if common_len > len(longest):
            longest = s1[:common_len]
    return longest
