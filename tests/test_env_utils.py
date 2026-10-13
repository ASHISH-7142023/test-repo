"""Unit tests for environment variable utility functions."""

import os
import unittest
from src.env_utils import (
    get_env_str,
    get_env_bool,
    get_env_int,
    get_env_float,
    get_env_list,
    require_env
)


class TestEnvUtils(unittest.TestCase):

    def setUp(self):
        self.orig_env = os.environ.copy()

    def tearDown(self):
        os.environ.clear()
        os.environ.update(self.orig_env)

    def test_get_env_str(self):
        os.environ["TEST_STR"] = "production"
        self.assertEqual(get_env_str("TEST_STR"), "production")
        self.assertEqual(get_env_str("NON_EXISTENT", "default_val"), "default_val")

    def test_get_env_bool(self):
        os.environ["BOOL_TRUE_1"] = "true"
        os.environ["BOOL_TRUE_2"] = "1"
        os.environ["BOOL_TRUE_3"] = "yes"
        os.environ["BOOL_FALSE"] = "false"
        self.assertTrue(get_env_bool("BOOL_TRUE_1"))
        self.assertTrue(get_env_bool("BOOL_TRUE_2"))
        self.assertTrue(get_env_bool("BOOL_TRUE_3"))
        self.assertFalse(get_env_bool("BOOL_FALSE"))
        self.assertFalse(get_env_bool("MISSING_BOOL", default=False))
        self.assertTrue(get_env_bool("MISSING_BOOL", default=True))

    def test_get_env_int(self):
        os.environ["TEST_INT"] = "8080"
        os.environ["TEST_BAD_INT"] = "not_a_number"
        self.assertEqual(get_env_int("TEST_INT"), 8080)
        self.assertEqual(get_env_int("TEST_BAD_INT", default=3000), 3000)
        self.assertEqual(get_env_int("MISSING_INT", default=5000), 5000)

    def test_get_env_float(self):
        os.environ["TEST_FLOAT"] = "3.1415"
        self.assertAlmostEqual(get_env_float("TEST_FLOAT"), 3.1415)
        self.assertAlmostEqual(get_env_float("MISSING_FLOAT", default=1.5), 1.5)

    def test_get_env_list(self):
        os.environ["TEST_LIST"] = "host1, host2 , host3"
        self.assertEqual(get_env_list("TEST_LIST"), ["host1", "host2", "host3"])
        self.assertEqual(get_env_list("MISSING_LIST", default=["a", "b"]), ["a", "b"])

    def test_require_env(self):
        os.environ["MANDATORY_KEY"] = "secret123"
        self.assertEqual(require_env("MANDATORY_KEY"), "secret123")
        with self.assertRaises(KeyError):
            require_env("DEFINITELY_MISSING_KEY")


if __name__ == "__main__":
    unittest.main()
