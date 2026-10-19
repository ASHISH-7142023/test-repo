import unittest
from src.totp_utils import hotp, totp, verify_totp, generate_totp_secret

class TestTOTP(unittest.TestCase):
    def test_rfc4226_test_vectors(self):
        secret = b"12345678901234567890"
        expected = ["755224", "287082", "359152", "969429", "338314"]
        for counter, code in enumerate(expected):
            self.assertEqual(hotp(secret, counter), code)

    def test_totp_verification_window(self):
        sec = generate_totp_secret()
        token = totp(sec, for_time=1000.0)
        self.assertTrue(verify_totp(token, sec, for_time=1000.0))
        self.assertTrue(verify_totp(token, sec, for_time=1025.0))
        self.assertFalse(verify_totp(token, sec, for_time=1100.0, window=1))

if __name__ == "__main__":
    unittest.main()
