import unittest
from src.semver_range import satisfies_range

class TestSemverRange(unittest.TestCase):
    def test_satisfies_range(self):
        self.assertTrue(satisfies_range("1.2.3", ">=1.0.0 <2.0.0"))
        self.assertFalse(satisfies_range("2.0.0", ">=1.0.0 <2.0.0"))
        self.assertTrue(satisfies_range("1.5.0", "^1.2.0"))
        self.assertFalse(satisfies_range("2.0.0", "^1.2.0"))
        self.assertTrue(satisfies_range("1.2.8", "~1.2.0"))
        self.assertFalse(satisfies_range("1.3.0", "~1.2.0"))

if __name__ == "__main__":
    unittest.main()
