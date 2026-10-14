"""Unit tests for PBKDF2-HMAC password hashing and verification."""

import unittest
from src.security_utils import generate_salt, hash_password, verify_password


class TestSecurityUtils(unittest.TestCase):

    def test_generate_salt(self):
        s1 = generate_salt(16)
        s2 = generate_salt(16)
        self.assertEqual(len(s1), 16)
        self.assertNotEqual(s1, s2)

    def test_hash_and_verify_success(self):
        password = "CorrectHorseBatteryStaple!2026"
        hashed = hash_password(password, iterations=10_000)
        self.assertTrue(hashed.startswith("$pbkdf2-sha256$10000$"))
        self.assertTrue(verify_password(password, hashed))

    def test_verify_failure_wrong_password(self):
        password = "SecretPassword123"
        hashed = hash_password(password, iterations=10_000)
        self.assertFalse(verify_password("WrongPassword456", hashed))

    def test_verify_invalid_hash_format(self):
        with self.assertRaises(ValueError):
            verify_password("test", "invalid_hash_string")


if __name__ == "__main__":
    unittest.main()
