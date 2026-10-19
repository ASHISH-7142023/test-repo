"""
ISBN-10 & ISBN-13 Validation, Checksum, and Conversion Utilities.
"""
import re

def _clean_isbn(isbn: str) -> str:
    return re.sub(r"[\s\-]", "", isbn).upper()

def calculate_isbn10_check_digit(prefix9: str) -> str:
    """Calculate the 10th check digit for a 9-digit prefix."""
    digits = [int(c) for c in prefix9]
    if len(digits) != 9:
        raise ValueError("Prefix must be exactly 9 digits")
    s = sum((10 - i) * d for i, d in enumerate(digits))
    rem = (11 - (s % 11)) % 11
    return "X" if rem == 10 else str(rem)

def validate_isbn10(isbn: str) -> bool:
    """Validate a 10-digit ISBN string."""
    clean = _clean_isbn(isbn)
    if len(clean) != 10:
        return False
    if not clean[:9].isdigit():
        return False
    expected = calculate_isbn10_check_digit(clean[:9])
    return clean[9] == expected

def calculate_isbn13_check_digit(prefix12: str) -> str:
    """Calculate the 13th check digit for a 12-digit prefix."""
    digits = [int(c) for c in prefix12]
    if len(digits) != 12:
        raise ValueError("Prefix must be exactly 12 digits")
    s = sum(d * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits))
    rem = (10 - (s % 10)) % 10
    return str(rem)

def validate_isbn13(isbn: str) -> bool:
    """Validate a 13-digit ISBN string."""
    clean = _clean_isbn(isbn)
    if len(clean) != 13 or not clean.isdigit():
        return False
    expected = calculate_isbn13_check_digit(clean[:12])
    return clean[12] == expected

def isbn10_to_isbn13(isbn10: str) -> str:
    """Convert a valid 10-digit ISBN to a 13-digit ISBN."""
    clean = _clean_isbn(isbn10)
    if not validate_isbn10(clean):
        raise ValueError("Invalid ISBN-10")
    prefix12 = "978" + clean[:9]
    check = calculate_isbn13_check_digit(prefix12)
    return prefix12 + check

def format_isbn(isbn: str) -> str:
    """Format and normalize an ISBN string."""
    clean = _clean_isbn(isbn)
    if validate_isbn10(clean):
        return f"{clean[0]}-{clean[1:4]}-{clean[4:9]}-{clean[9]}"
    elif validate_isbn13(clean):
        return f"{clean[:3]}-{clean[3]}-{clean[4:7]}-{clean[7:12]}-{clean[12]}"
    return clean
