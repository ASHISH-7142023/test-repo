"""Unit tests for input validation utilities."""

import unittest
from src.validators import is_valid_email, is_valid_url, is_strong_password, validate_required_keys


class TestValidators(unittest.TestCase):

    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("developer@example.com"))
        self.assertTrue(is_valid_email("user.name+tag@sub.domain.co"))
        self.assertFalse(is_valid_email("invalid-email"))
        self.assertFalse(is_valid_email("@domain.com"))
        self.assertFalse(is_valid_email(""))

    def test_is_valid_url(self):
        self.assertTrue(is_valid_url("https://github.com/ASHISH-7142023/test-repo"))
        self.assertTrue(is_valid_url("http://example.com/api/v1?page=1"))
        self.assertFalse(is_valid_url("ftp://server.org"))
        self.assertFalse(is_valid_url("just_text"))

    def test_is_strong_password(self):
        valid, issues = is_strong_password("Secret123!Secure")
        self.assertTrue(valid)
        self.assertEqual(len(issues), 0)

        valid_weak, issues_weak = is_strong_password("weak")
        self.assertFalse(valid_weak)
        self.assertGreater(len(issues_weak), 0)

    def test_validate_required_keys(self):
        payload = {"name": "Test", "version": "1.0", "active": True}
        valid, missing = validate_required_keys(payload, ["name", "version"])
        self.assertTrue(valid)
        self.assertEqual(missing, [])

        valid_fail, missing_fail = validate_required_keys(payload, ["name", "description"])
        self.assertFalse(valid_fail)
        self.assertEqual(missing_fail, ["description"])


if __name__ == "__main__":
    unittest.main()
