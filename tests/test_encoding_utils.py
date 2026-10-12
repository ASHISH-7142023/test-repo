"""Unit tests for data encoding and decoding utilities."""

import unittest
from src.encoding_utils import to_base64, from_base64, to_hex, from_hex, url_encode, url_decode


class TestEncodingUtils(unittest.TestCase):

    def test_base64_roundtrip(self):
        text = "DevToolkit 2026 Test String! 🚀"
        encoded = to_base64(text)
        decoded = from_base64(encoded)
        self.assertEqual(decoded, text)

    def test_base64_url_safe(self):
        text = "subjects?query=a&b=c+d"
        encoded = to_base64(text, url_safe=True)
        self.assertNotIn("+", encoded)
        self.assertNotIn("/", encoded)
        self.assertEqual(from_base64(encoded, url_safe=True), text)

    def test_hex_roundtrip(self):
        text = "Hello Hexadecimal!"
        hex_str = to_hex(text)
        self.assertEqual(from_hex(hex_str), text)

    def test_url_encoding(self):
        raw = "name=John Doe&status=active 100%"
        encoded = url_encode(raw)
        self.assertEqual(url_decode(encoded), raw)


if __name__ == "__main__":
    unittest.main()
