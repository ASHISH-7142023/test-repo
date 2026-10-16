"""Luhn algorithm (Modulus 10) calculation and card number verification."""


def validate_luhn(card_number: str) -> bool:
    """Verify whether numeric string passes Luhn modulus 10 checksum."""
    clean = card_number.replace(" ", "").replace("-", "")
    if not clean.isdigit() or len(clean) < 2:
        return False

    digits = [int(d) for d in clean]
    checksum = 0
    reverse_digits = digits[::-1]

    for idx, d in enumerate(reverse_digits):
        if idx % 2 == 1:
            doubled = d * 2
            checksum += doubled if doubled < 10 else (doubled - 9)
        else:
            checksum += d

    return checksum % 10 == 0


def calculate_luhn_digit(partial_number: str) -> int:
    """Compute the check digit required to make partial_number satisfy Luhn algorithm."""
    clean = partial_number.replace(" ", "").replace("-", "")
    if not clean.isdigit():
        raise ValueError("Input must consist solely of digits.")
    digits = [int(d) for d in clean]
    checksum = 0
    # Next digit will be at index 0 (even), so existing digits are weighted from 1
    for idx, d in enumerate(digits[::-1]):
        if idx % 2 == 0:
            doubled = d * 2
            checksum += doubled if doubled < 10 else (doubled - 9)
        else:
            checksum += d

    return (10 - (checksum % 10)) % 10
