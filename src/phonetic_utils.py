"""Phonetic string encoding algorithms including American Soundex."""

import re

SOUNDEX_MAP = {
    "B": "1", "F": "1", "P": "1", "V": "1",
    "C": "2", "G": "2", "J": "2", "K": "2", "Q": "2", "S": "2", "X": "2", "Z": "2",
    "D": "3", "T": "3",
    "L": "4",
    "M": "5", "N": "5",
    "R": "6",
}


def soundex(name: str) -> str:
    """Encode an English name into its 4-character Soundex code."""
    name = re.sub(r"[^A-Za-z]", "", name).upper()
    if not name:
        return "0000"

    first_letter = name[0]
    codes = [first_letter]

    prev_code = SOUNDEX_MAP.get(first_letter, "")

    for char in name[1:]:
        curr_code = SOUNDEX_MAP.get(char, "")
        if curr_code != prev_code:
            if curr_code != "":
                codes.append(curr_code)
            prev_code = curr_code

    code_str = "".join(codes)
    return (code_str + "0000")[:4]


def soundex_matches(name1: str, name2: str) -> bool:
    """Check if two names have identical Soundex phonetic representations."""
    return soundex(name1) == soundex(name2)
