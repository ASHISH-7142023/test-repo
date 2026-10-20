import unittest
from src.rle_compression import rle_encode, rle_decode, rle_encode_bytes, rle_decode_bytes

class TestRLECompression(unittest.TestCase):
    def test_text_rle(self):
        text = "WWWWWWAAAAABBBCCCD"
        encoded = rle_encode(text)
        self.assertEqual(encoded, "6W5A3B3CD")
        self.assertEqual(rle_decode(encoded), text)

    def test_bytes_rle(self):
        data = b"\x00" * 50 + b"\xff" * 20
        enc = rle_encode_bytes(data)
        self.assertEqual(len(enc), 4)
        self.assertEqual(rle_decode_bytes(enc), data)

if __name__ == "__main__":
    unittest.main()
