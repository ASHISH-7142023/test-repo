"""
BitField packing and unpacking utilities.
Packs multiple named integer fields of arbitrary bit widths into a single integer or bytes.
"""
from typing import Dict, Any, List, Tuple

class BitField:
    """
    Defines a specification of fields: [(name, bit_width), ...]
    and provides packing and unpacking.
    """
    def __init__(self, fields: List[Tuple[str, int]]):
        self.fields = fields
        self.total_bits = sum(width for _, width in fields)
        self.total_bytes = (self.total_bits + 7) // 8

    def pack(self, **kwargs) -> int:
        result = 0
        shift = self.total_bits
        for name, width in self.fields:
            val = kwargs.get(name, 0)
            max_val = (1 << width) - 1
            if val < 0 or val > max_val:
                raise ValueError(f"Value {val} for '{name}' out of range [0, {max_val}]")
            shift -= width
            result |= (val << shift)
        return result

    def unpack(self, packed_int: int) -> Dict[str, int]:
        result = {}
        shift = self.total_bits
        for name, width in self.fields:
            shift -= width
            mask = (1 << width) - 1
            result[name] = (packed_int >> shift) & mask
        return result

    def pack_bytes(self, **kwargs) -> bytes:
        val = self.pack(**kwargs)
        return val.to_bytes(self.total_bytes, byteorder="big")

    def unpack_bytes(self, data: bytes) -> Dict[str, int]:
        val = int.from_bytes(data, byteorder="big")
        return self.unpack(val)
