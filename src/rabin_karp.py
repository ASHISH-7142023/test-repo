"""Rabin-Karp polynomial rolling hash string matching algorithm."""

from typing import List


def rabin_karp_search(text: str, pattern: str, prime: int = 101, base: int = 256) -> List[int]:
    """Find all starting indices of pattern in text using rolling hash."""
    if not pattern:
        return []
    n = len(text)
    m = len(pattern)
    if m > n:
        return []

    h = pow(base, m - 1, prime)

    p_hash = 0
    t_hash = 0
    matches = []

    for i in range(m):
        p_hash = (base * p_hash + ord(pattern[i])) % prime
        t_hash = (base * t_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i : i + m] == pattern:
                matches.append(i)

        if i < n - m:
            t_hash = (base * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t_hash < 0:
                t_hash += prime

    return matches


def rabin_karp_contains(text: str, pattern: str) -> bool:
    """Return True if pattern exists in text."""
    if not pattern:
        return True
    return len(rabin_karp_search(text, pattern)) > 0
