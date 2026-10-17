"""Base58 encoding and decoding utilities using the Bitcoin alphabet."""

import hashlib
from typing import Union

ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
BASE = len(ALPHABET)
INDEX_MAP = {c: i for i, c in enumerate(ALPHABET)}


def b58encode(data: Union[bytes, str]) -> str:
    """Encode bytes or string into a Base58 string."""
    if isinstance(data, str):
        data = data.encode("utf-8")

    leading_zeros = 0
    for b in data:
        if b == 0:
            leading_zeros += 1
        else:
            break

    num = int.from_bytes(data, byteorder="big")
    res = []
    while num > 0:
        num, rem = divmod(num, BASE)
        res.append(ALPHABET[rem])

    res.reverse()
    return (ALPHABET[0] * leading_zeros) + "".join(res)


def b58decode(s: str) -> bytes:
    """Decode a Base58 string back to bytes."""
    leading_ones = 0
    for c in s:
        if c == ALPHABET[0]:
            leading_ones += 1
        else:
            break

    num = 0
    for c in s:
        if c not in INDEX_MAP:
            raise ValueError(f"Invalid Base58 character: '{c}'")
        num = num * BASE + INDEX_MAP[c]

    byte_list = []
    while num > 0:
        num, rem = divmod(num, 256)
        byte_list.append(rem)

    byte_list.reverse()
    return (bytes([0]) * leading_ones) + bytes(byte_list)


def b58encode_check(data: bytes) -> str:
    """Encode data with a 4-byte double SHA-256 checksum."""
    h1 = hashlib.sha256(data).digest()
    checksum = hashlib.sha256(h1).digest()[:4]
    return b58encode(data + checksum)


def b58decode_check(s: str) -> bytes:
    """Decode data and verify its 4-byte double SHA-256 checksum."""
    raw = b58decode(s)
    if len(raw) < 4:
        raise ValueError("Invalid Base58Check data: length too short")
    payload, checksum = raw[:-4], raw[-4:]
    h1 = hashlib.sha256(payload).digest()
    expected_checksum = hashlib.sha256(h1).digest()[:4]
    if checksum != expected_checksum:
        raise ValueError("Checksum verification failed")
    return payload
