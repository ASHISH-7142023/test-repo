import unittest
from src.bit_field import BitField

class TestBitField(unittest.TestCase):
    def test_pack_and_unpack(self):
        bf = BitField([("flag", 1), ("type", 3), ("value", 8)])
        packed = bf.pack(flag=1, type=5, value=200)
        unpacked = bf.unpack(packed)
        self.assertEqual(unpacked, {"flag": 1, "type": 5, "value": 200})

    def test_pack_bytes(self):
        bf = BitField([("a", 4), ("b", 4)])
        b = bf.pack_bytes(a=15, b=0)
        self.assertEqual(b, b"\xf0")
        self.assertEqual(bf.unpack_bytes(b), {"a": 15, "b": 0})

if __name__ == "__main__":
    unittest.main()
