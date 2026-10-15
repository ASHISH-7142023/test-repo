"""Unit tests for semantic versioning utilities."""

import unittest
from src.semver_utils import parse_semver, is_valid_semver, compare_semver, bump_semver


class TestSemverUtils(unittest.TestCase):

    def test_parse_and_validate(self):
        self.assertTrue(is_valid_semver("1.2.3"))
        self.assertTrue(is_valid_semver("v2.0.1-alpha.1"))
        self.assertFalse(is_valid_semver("1.2"))
        self.assertEqual(parse_semver("1.10.4"), (1, 10, 4))

    def test_compare_semver(self):
        self.assertEqual(compare_semver("1.0.0", "1.0.0"), 0)
        self.assertEqual(compare_semver("1.2.0", "1.1.9"), 1)
        self.assertEqual(compare_semver("1.2.3", "1.2.4"), -1)

    def test_bump_semver(self):
        self.assertEqual(bump_semver("1.2.3", "patch"), "1.2.4")
        self.assertEqual(bump_semver("1.2.3", "minor"), "1.3.0")
        self.assertEqual(bump_semver("1.2.3", "major"), "2.0.0")


if __name__ == "__main__":
    unittest.main()
