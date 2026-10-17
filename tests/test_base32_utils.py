import unittest
from src.base32_utils import base32_encode, base32_decode

class TestBase32Utils(unittest.TestCase):
    def test_rfc4648_test_vectors(self):
        self.assertEqual(base32_encode(""), "")
        self.assertEqual(base32_encode("f"), "MY======")
        self.assertEqual(base32_encode("fo"), "MZXQ====")
        self.assertEqual(base32_encode("foo"), "MZXW6===")
        self.assertEqual(base32_encode("foobar"), "MZXW6YTBOI======")

    def test_decode_vectors(self):
        self.assertEqual(base32_decode("MZXW6===").decode(), "foo")
        self.assertEqual(base32_decode("mzxw6ytboi======").decode(), "foobar")
        self.assertEqual(base32_decode("MZXW6").decode(), "foo")

if __name__ == "__main__":
    unittest.main()
