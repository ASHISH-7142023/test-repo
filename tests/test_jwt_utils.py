"""Unit tests for JWT encoding and decoding utilities."""

import time
import unittest
from src.jwt_utils import encode_jwt, decode_jwt


class TestJwtUtils(unittest.TestCase):

    def test_encode_and_decode_valid(self):
        secret = "super-secret-key-12345"
        payload = {"sub": "user_101", "role": "admin"}
        token = encode_jwt(payload, secret)
        self.assertEqual(token.count("."), 2)

        decoded = decode_jwt(token, secret)
        self.assertEqual(decoded["sub"], "user_101")
        self.assertEqual(decoded["role"], "admin")

    def test_tampered_signature_fails(self):
        secret = "secret-key"
        token = encode_jwt({"user": "alice"}, secret)
        tampered = token[:-4] + "fake"
        with self.assertRaises(ValueError):
            decode_jwt(tampered, secret)

    def test_expired_token_fails(self):
        secret = "secret-key"
        expired_payload = {"user": "bob", "exp": time.time() - 10}
        token = encode_jwt(expired_payload, secret)
        with self.assertRaises(ValueError):
            decode_jwt(token, secret, verify_exp=True)


if __name__ == "__main__":
    unittest.main()
