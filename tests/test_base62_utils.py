import unittest
from src.base62_utils import (
    base62_encode_int, base62_decode_int,
    base62_encode_bytes, base62_decode_bytes
)

class TestBase62(unittest.TestCase):
    def test_int_roundtrip(self):
        for val in [0, 1, 61, 62, 12345, 9876543210]:
            self.assertEqual(base62_decode_int(base62_encode_int(val)), val)

    def test_bytes_roundtrip(self):
        sample = b"Hello Base62 World!"
        enc = base62_encode_bytes(sample)
        dec = base62_decode_bytes(enc)
        self.assertEqual(dec, sample)

if __name__ == "__main__":
    unittest.main()
