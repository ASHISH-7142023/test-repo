import unittest
from src.base58_utils import b58encode, b58decode, b58encode_check, b58decode_check

class TestBase58Utils(unittest.TestCase):
    def test_roundtrip(self):
        msg = b"Hello World!"
        encoded = b58encode(msg)
        self.assertEqual(encoded, "2NEpo7TZRRrLZSi2U")
        self.assertEqual(b58decode(encoded), msg)

    def test_leading_zeros(self):
        data = bytes([0, 0]) + b"abc"
        encoded = b58encode(data)
        self.assertTrue(encoded.startswith("11"))
        self.assertEqual(b58decode(encoded), data)

    def test_invalid_chars(self):
        with self.assertRaises(ValueError):
            b58decode("0OIl")

    def test_base58_check(self):
        data = b"secure-payload"
        chk_encoded = b58encode_check(data)
        decoded = b58decode_check(chk_encoded)
        self.assertEqual(decoded, data)

        with self.assertRaises(ValueError):
            b58decode_check(chk_encoded[:-1] + "X")

if __name__ == "__main__":
    unittest.main()
