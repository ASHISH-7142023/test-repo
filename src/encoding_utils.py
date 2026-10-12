"""Data encoding, decoding, and representation utilities."""

import base64
import urllib.parse


def to_base64(text: str, url_safe: bool = False) -> str:
    """Encode UTF-8 string to Base64 (standard or URL-safe)."""
    raw_bytes = text.encode("utf-8")
    if url_safe:
        return base64.urlsafe_b64encode(raw_bytes).decode("ascii")
    return base64.b64encode(raw_bytes).decode("ascii")


def from_base64(encoded: str, url_safe: bool = False) -> str:
    """Decode Base64 string to original UTF-8 string."""
    raw_bytes = encoded.encode("ascii")
    if url_safe:
        return base64.urlsafe_b64decode(raw_bytes).decode("utf-8")
    return base64.b64decode(raw_bytes).decode("utf-8")


def to_hex(text: str) -> str:
    """Convert string characters to hexadecimal representation."""
    return text.encode("utf-8").hex()


def from_hex(hex_str: str) -> str:
    """Convert hexadecimal representation back to original string."""
    return bytes.fromhex(hex_str).decode("utf-8")


def url_encode(text: str) -> str:
    """Escape string for safe URL query parameters."""
    return urllib.parse.quote_plus(text)


def url_decode(text: str) -> str:
    """Unescape URL encoded string."""
    return urllib.parse.unquote_plus(text)
