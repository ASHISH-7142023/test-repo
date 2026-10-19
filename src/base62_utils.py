"""
Base62 Encoding and Decoding Utilities.
Standard alphanumeric charset [0-9A-Za-z] for URL shorteners and token compacting.
"""
BASE62_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
BASE62_LOOKUP = {c: i for i, c in enumerate(BASE62_ALPHABET)}

def base62_encode_int(num: int) -> str:
    """Encode a non-negative integer into Base62 string."""
    if num < 0:
        raise ValueError("num must be non-negative")
    if num == 0:
        return BASE62_ALPHABET[0]
    chars = []
    while num > 0:
        num, rem = divmod(num, 62)
        chars.append(BASE62_ALPHABET[rem])
    chars.reverse()
    return "".join(chars)

def base62_decode_int(s: str) -> int:
    """Decode a Base62 string back into an integer."""
    if not s:
        raise ValueError("Input string cannot be empty")
    res = 0
    for char in s:
        if char not in BASE62_LOOKUP:
            raise ValueError(f"Invalid Base62 character: {char}")
        res = res * 62 + BASE62_LOOKUP[char]
    return res

def base62_encode_bytes(data: bytes) -> str:
    """Encode bytes into Base62."""
    if not data:
        return ""
    leading_zeros = len(data) - len(data.lstrip(b"\x00"))
    num = int.from_bytes(data, byteorder="big")
    encoded = base62_encode_int(num) if num > 0 else ""
    return (BASE62_ALPHABET[0] * leading_zeros) + encoded

def base62_decode_bytes(s: str) -> bytes:
    """Decode Base62 string back into bytes."""
    if not s:
        return b""
    leading_zeros = len(s) - len(s.lstrip(BASE62_ALPHABET[0]))
    non_zeros = s.lstrip(BASE62_ALPHABET[0])
    if not non_zeros:
        return bytes([0] * leading_zeros)
    num = base62_decode_int(non_zeros)
    num_bytes = (num.bit_length() + 7) // 8
    raw = num.to_bytes(num_bytes, byteorder="big")
    return (bytes([0] * leading_zeros)) + raw
