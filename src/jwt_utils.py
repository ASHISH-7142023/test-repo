"""Lightweight zero-dependency JSON Web Token (JWT) implementation using HMAC-SHA256."""

import json
import time
import hmac
import hashlib
import base64
from typing import Any, Dict


def _b64_url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")


def _b64_url_decode(s: str) -> bytes:
    padding = "=" * ((4 - len(s) % 4) % 4)
    return base64.urlsafe_b64decode((s + padding).encode("ascii"))


def encode_jwt(payload: Dict[str, Any], secret: str, algorithm: str = "HS256") -> str:
    """Encode payload dictionary into signed JWT string."""
    if algorithm != "HS256":
        raise ValueError("Only HS256 algorithm is currently supported.")
    header = {"alg": "HS256", "typ": "JWT"}
    hdr_b64 = _b64_url_encode(json.dumps(header, separators=(",", ":")).encode("utf-8"))
    payload_b64 = _b64_url_encode(json.dumps(payload, separators=(",", ":")).encode("utf-8"))

    signing_input = f"{hdr_b64}.{payload_b64}".encode("ascii")
    signature = hmac.new(secret.encode("utf-8"), signing_input, hashlib.sha256).digest()
    sig_b64 = _b64_url_encode(signature)
    return f"{hdr_b64}.{payload_b64}.{sig_b64}"


def decode_jwt(token: str, secret: str, verify_exp: bool = True) -> Dict[str, Any]:
    """Decode and verify JWT signature and optional expiration claim."""
    parts = token.strip().split(".")
    if len(parts) != 3:
        raise ValueError("Invalid JWT token format.")
    hdr_b64, payload_b64, sig_b64 = parts

    signing_input = f"{hdr_b64}.{payload_b64}".encode("ascii")
    expected_sig = hmac.new(secret.encode("utf-8"), signing_input, hashlib.sha256).digest()
    actual_sig = _b64_url_decode(sig_b64)

    if not hmac.compare_digest(expected_sig, actual_sig):
        raise ValueError("Invalid JWT signature.")

    payload = json.loads(_b64_url_decode(payload_b64).decode("utf-8"))
    if verify_exp and "exp" in payload:
        if time.time() > float(payload["exp"]):
            raise ValueError("JWT token has expired.")
    return payload
