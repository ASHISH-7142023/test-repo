"""
Run-Length Encoding (RLE) for text and byte streams.
Zero external dependencies.
"""
import re

def rle_encode(text: str) -> str:
    """Encode string into RLE (e.g. 'AAAABBBCC' -> '4A3B2C'). Single characters are preserved."""
    if not text:
        return ""
    res = []
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        count = 1
        while i + 1 < n and text[i + 1] == c:
            count += 1
            i += 1
        if count > 1:
            res.append(f"{count}{c}")
        else:
            res.append(c)
        i += 1
    return "".join(res)

def rle_decode(encoded: str) -> str:
    """Decode RLE string back to plain string."""
    if not encoded:
        return ""
    res = []
    tokens = re.findall(r"(\d*)([^\d])", encoded)
    for count_str, char in tokens:
        count = int(count_str) if count_str else 1
        res.append(char * count)
    return "".join(res)

def rle_encode_bytes(data: bytes) -> bytes:
    """Encode bytes into byte pairs (count, byte). Count up to 255."""
    if not data:
        return b""
    res = bytearray()
    i = 0
    n = len(data)
    while i < n:
        b = data[i]
        count = 1
        while i + 1 < n and data[i + 1] == b and count < 255:
            count += 1
            i += 1
        res.append(count)
        res.append(b)
        i += 1
    return bytes(res)

def rle_decode_bytes(encoded: bytes) -> bytes:
    """Decode byte-pair RLE back to raw bytes."""
    if len(encoded) % 2 != 0:
        raise ValueError("Invalid RLE byte stream: odd length")
    res = bytearray()
    for i in range(0, len(encoded), 2):
        count = encoded[i]
        b = encoded[i + 1]
        res.extend(bytes([b]) * count)
    return bytes(res)
