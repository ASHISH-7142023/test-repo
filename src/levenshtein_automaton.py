"""
Levenshtein Automaton & Fuzzy Search.
Provides state-based / dynamic matrix fuzzy matching within edit distance k.
"""
from typing import List, Tuple

def levenshtein_distance(s1: str, s2: str) -> int:
    """Compute standard Levenshtein distance between two strings."""
    if s1 == s2:
        return 0
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)
    prev = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr = [i + 1] * (len(s2) + 1)
        for j, c2 in enumerate(s2):
            cost = 0 if c1 == c2 else 1
            curr[j + 1] = min(prev[j + 1] + 1, curr[j] + 1, prev[j] + cost)
        prev = curr
    return prev[-1]

class LevenshteinAutomaton:
    """
    Automaton state evaluator for pattern within max_edits.
    """
    def __init__(self, pattern: str, max_edits: int):
        self.pattern = pattern
        self.max_edits = max_edits

    def evaluate(self, candidate: str) -> Tuple[bool, int]:
        dist = levenshtein_distance(self.pattern, candidate)
        return (dist <= self.max_edits, dist)

    def filter_dictionary(self, dictionary: List[str]) -> List[Tuple[str, int]]:
        results = []
        for word in dictionary:
            match, dist = self.evaluate(word)
            if match:
                results.append((word, dist))
        results.sort(key=lambda x: (x[1], x[0]))
        return results

def fuzzy_search(pattern: str, max_edits: int, dictionary: List[str]) -> List[Tuple[str, int]]:
    """Helper function to find all words within max_edits."""
    automaton = LevenshteinAutomaton(pattern, max_edits)
    return automaton.filter_dictionary(dictionary)
