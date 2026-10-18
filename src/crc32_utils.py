"""Pure-Python IEEE 802.3 CRC32 checksum calculator."""

from typing import Union

CRC32_TABLE = []
for i in range(256):
    crc = i
    for _ in range(8):
        if crc & 1:
            crc = (crc >> 1) ^ 0xEDB88320
        else:
            crc >>= 1
    CRC32_TABLE.append(crc)


def crc32_compute(data: Union[bytes, str]) -> int:
    """Compute unsigned 32-bit CRC32 checksum."""
    if isinstance(data, str):
        data = data.encode("utf-8")
    crc = 0xFFFFFFFF
    for b in data:
        crc = (crc >> 8) ^ CRC32_TABLE[(crc ^ b) & 0xFF]
    return (crc ^ 0xFFFFFFFF) & 0xFFFFFFFF


def crc32_hex(data: Union[bytes, str]) -> str:
    """Compute CRC32 checksum as 8-character lowercase hexadecimal string."""
    return f"{crc32_compute(data):08x}"
