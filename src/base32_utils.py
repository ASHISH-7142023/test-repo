"""Base32 RFC 4648 encoding and decoding utilities."""

import base64
from typing import Union


def base32_encode(data: Union[bytes, str], pad: bool = True) -> str:
    """Encode bytes or string to RFC 4648 Base32 string."""
    if isinstance(data, str):
        data = data.encode("utf-8")
    encoded = base64.b32encode(data).decode("ascii")
    if not pad:
        encoded = encoded.rstrip("=")
    return encoded


def base32_decode(data: str) -> bytes:
    """Decode an RFC 4648 Base32 string back to bytes."""
    s = data.strip().upper()
    missing_padding = len(s) % 8
    if missing_padding != 0:
        s += "=" * (8 - missing_padding)
    return base64.b32decode(s.encode("ascii"))
