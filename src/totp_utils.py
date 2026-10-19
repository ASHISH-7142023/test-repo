"""
TOTP & HOTP (RFC 6238 & RFC 4226) Authentication Utilities.
Zero external dependencies, uses Python hashlib and hmac.
"""
import hmac
import hashlib
import time
import base64
import struct
import secrets
from typing import Union

def _normalize_secret(secret: Union[str, bytes]) -> bytes:
    if isinstance(secret, str):
        clean = secret.replace(" ", "").upper()
        missing_padding = len(clean) % 8
        if missing_padding != 0:
            clean += "=" * (8 - missing_padding)
        try:
            return base64.b32decode(clean, casefold=True)
        except Exception:
            return secret.encode("utf-8")
    return secret

def hotp(secret: Union[str, bytes], counter: int, digits: int = 6, digest: str = "sha1") -> str:
    """
    Compute RFC 4226 HMAC-Based One-Time Password (HOTP).
    """
    key = _normalize_secret(secret)
    msg = struct.pack(">Q", counter)
    hasher = getattr(hashlib, digest.lower(), hashlib.sha1)
    h = hmac.new(key, msg, hasher).digest()

    offset = h[-1] & 0x0F
    code = struct.unpack(">I", h[offset:offset + 4])[0] & 0x7FFFFFFF
    token = code % (10 ** digits)
    return str(token).zfill(digits)

def totp(
    secret: Union[str, bytes],
    time_step: int = 30,
    for_time: float = None,
    digits: int = 6,
    digest: str = "sha1"
) -> str:
    """
    Compute RFC 6238 Time-Based One-Time Password (TOTP).
    """
    current_time = for_time if for_time is not None else time.time()
    counter = int(current_time // time_step)
    return hotp(secret, counter, digits=digits, digest=digest)

def verify_totp(
    token: str,
    secret: Union[str, bytes],
    time_step: int = 30,
    window: int = 1,
    for_time: float = None
) -> bool:
    """
    Verify a TOTP token allowing a +/- window of time steps for clock drift.
    """
    current_time = for_time if for_time is not None else time.time()
    base_counter = int(current_time // time_step)
    for offset in range(-window, window + 1):
        if hotp(secret, base_counter + offset, digits=len(token)) == token:
            return True
    return False

def generate_totp_secret(length: int = 20) -> str:
    """Generate a random Base32 TOTP secret string."""
    random_bytes = secrets.token_bytes(length)
    return base64.b32encode(random_bytes).decode("ascii").replace("=", "")
