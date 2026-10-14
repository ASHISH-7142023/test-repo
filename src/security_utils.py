"""Cryptographic password hashing and verification using PBKDF2-HMAC-SHA256."""

import os
import hashlib
import hmac
from typing import Tuple


def generate_salt(length: int = 16) -> bytes:
    """Generate cryptographically secure random salt bytes."""
    return os.urandom(length)


def hash_password(password: str, salt: bytes = None, iterations: int = 100_000) -> str:
    """
    Hash a password using PBKDF2-HMAC-SHA256.
    Returns format: '$pbkdf2-sha256$iterations$salt_hex$hash_hex'
    """
    if salt is None:
        salt = generate_salt(16)
    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    salt_hex = salt.hex()
    hash_hex = key.hex()
    return f"$pbkdf2-sha256${iterations}${salt_hex}${hash_hex}"


def verify_password(password: str, hashed_str: str) -> bool:
    """Verify password against formatted PBKDF2 string in constant time."""
    parts = hashed_str.split("$")
    if len(parts) != 5 or parts[1] != "pbkdf2-sha256":
        raise ValueError("Invalid password hash format.")
    iterations = int(parts[2])
    salt = bytes.fromhex(parts[3])
    expected_hash = parts[4]
    computed_key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return hmac.compare_digest(computed_key.hex(), expected_hash)
