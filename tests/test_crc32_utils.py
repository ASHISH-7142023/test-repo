import unittest
import zlib
from src.crc32_utils import crc32_compute, crc32_hex

class TestCRC32Utils(unittest.TestCase):
    def test_matches_zlib(self):
        for sample in [b"hello", b"123456789", b"DevToolkit CRC Test"]:
            self.assertEqual(crc32_compute(sample), zlib.crc32(sample))

    def test_crc32_hex(self):
        self.assertEqual(crc32_hex("123456789"), "cbf43926")

if __name__ == "__main__":
    unittest.main()
