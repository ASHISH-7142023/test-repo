"""
Pure-Python 32-bit MurmurHash3 (x86_32).
Fast, non-cryptographic hash function with excellent distribution.
"""
def murmurhash3_32(key: bytes, seed: int = 0) -> int:
    """Computes 32-bit MurmurHash3."""
    c1 = 0xcc9e2d51
    c2 = 0x1b873593
    r1 = 15
    r2 = 13
    m = 5
    n = 0xe6546b64

    h1 = seed & 0xFFFFFFFF
    length = len(key)
    nblocks = length // 4

    for i in range(nblocks):
        start = i * 4
        k1 = (
            key[start] |
            (key[start + 1] << 8) |
            (key[start + 2] << 16) |
            (key[start + 3] << 24)
        )
        k1 = (k1 * c1) & 0xFFFFFFFF
        k1 = ((k1 << r1) | (k1 >> (32 - r1))) & 0xFFFFFFFF
        k1 = (k1 * c2) & 0xFFFFFFFF

        h1 ^= k1
        h1 = ((h1 << r2) | (h1 >> (32 - r2))) & 0xFFFFFFFF
        h1 = ((h1 * m) + n) & 0xFFFFFFFF

    tail = key[nblocks * 4:]
    k1 = 0
    tail_len = len(tail)
    if tail_len == 3:
        k1 ^= tail[2] << 16
    if tail_len >= 2:
        k1 ^= tail[1] << 8
    if tail_len >= 1:
        k1 ^= tail[0]
        k1 = (k1 * c1) & 0xFFFFFFFF
        k1 = ((k1 << r1) | (k1 >> (32 - r1))) & 0xFFFFFFFF
        k1 = (k1 * c2) & 0xFFFFFFFF
        h1 ^= k1

    h1 ^= length
    h1 ^= (h1 >> 16)
    h1 = (h1 * 0x85ebca6b) & 0xFFFFFFFF
    h1 ^= (h1 >> 13)
    h1 = (h1 * 0xc2b2ae35) & 0xFFFFFFFF
    h1 ^= (h1 >> 16)

    return h1
