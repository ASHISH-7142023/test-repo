"""Unit tests for cryptographic utilities."""

import unittest
from src.crypto_utils import generate_secure_token, hash_sha256, constant_time_compare


class TestCryptoUtils(unittest.TestCase):

    def test_secure_token_uniqueness(self):
        t1 = generate_secure_token(32)
        t2 = generate_secure_token(32)
        self.assertNotEqual(t1, t2)
        self.assertGreater(len(t1), 32)

    def test_hash_sha256(self):
        h = hash_sha256("DevToolkit")
        self.assertEqual(len(h), 64)
        # Consistent output for identical inputs
        self.assertEqual(h, hash_sha256("DevToolkit"))
        self.assertNotEqual(h, hash_sha256("devtoolkit"))

    def test_constant_time_compare(self):
        self.assertTrue(constant_time_compare("secret_token_123", "secret_token_123"))
        self.assertFalse(constant_time_compare("secret_token_123", "different_token_456"))


if __name__ == "__main__":
    unittest.main()
