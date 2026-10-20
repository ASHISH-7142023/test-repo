import unittest
from src.murmurhash3 import murmurhash3_32

class TestMurmurHash3(unittest.TestCase):
    def test_murmurhash3(self):
        h = murmurhash3_32(b"hello world", seed=0)
        self.assertIsInstance(h, int)
        self.assertEqual(h, murmurhash3_32(b"hello world", seed=0))
        self.assertNotEqual(h, murmurhash3_32(b"hello world", seed=42))

if __name__ == "__main__":
    unittest.main()
