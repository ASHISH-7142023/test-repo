"""Input validation utilities for strings, credentials, and data payloads."""

import re
from typing import Dict, Any, List, Tuple


EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
URL_REGEX = re.compile(r"^https?://[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+(?:/[^\s]*)?$")


def is_valid_email(email: str) -> bool:
    """Validate format of an email address."""
    if not email or len(email) > 254:
        return False
    return bool(EMAIL_REGEX.match(email.strip()))


def is_valid_url(url: str) -> bool:
    """Validate format of an HTTP/HTTPS web URL."""
    if not url or len(url) > 2048:
        return False
    return bool(URL_REGEX.match(url.strip()))


def is_strong_password(password: str, min_length: int = 8) -> Tuple[bool, List[str]]:
    """
    Check if password satisfies security complexity criteria:
    - Minimum length
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    issues = []
    if not password or len(password) < min_length:
        issues.append(f"Password must be at least {min_length} characters long.")
    if not re.search(r"[A-Z]", password or ""):
        issues.append("Password must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password or ""):
        issues.append("Password must contain at least one lowercase letter.")
    if not re.search(r"\d", password or ""):
        issues.append("Password must contain at least one numeric digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password or ""):
        issues.append("Password must contain at least one special character.")
    return len(issues) == 0, issues


def validate_required_keys(data: Dict[str, Any], required_keys: List[str]) -> Tuple[bool, List[str]]:
    """Verify that all required keys are present and not None in dictionary."""
    missing = [key for key in required_keys if key not in data or data[key] is None]
    return len(missing) == 0, missing
