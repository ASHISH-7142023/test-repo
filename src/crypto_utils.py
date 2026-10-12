"""Cryptographic and secure token generation helpers."""

import secrets
import hashlib
import hmac


def generate_secure_token(nbytes: int = 32) -> str:
    """Generate a cryptographically secure URL-safe random string token."""
    return secrets.token_urlsafe(nbytes)


def hash_sha256(text: str) -> str:
    """Calculate the SHA-256 hexadecimal digest of text string."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def constant_time_compare(val1: str, val2: str) -> bool:
    """Compare two strings in constant time to prevent timing analysis attacks."""
    return hmac.compare_digest(val1.encode("utf-8"), val2.encode("utf-8"))
