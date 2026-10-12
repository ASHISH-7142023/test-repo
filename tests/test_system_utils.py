"""Unit tests for system diagnostics and formatters."""

import unittest
from src.system_utils import get_platform_info, format_bytes, get_disk_usage


class TestSystemUtils(unittest.TestCase):

    def test_get_platform_info(self):
        info = get_platform_info()
        self.assertIn("system", info)
        self.assertIn("python_version", info)
        self.assertTrue(len(info["system"]) > 0)

    def test_format_bytes(self):
        self.assertEqual(format_bytes(0), "0.00 B")
        self.assertEqual(format_bytes(1024), "1.00 KB")
        self.assertEqual(format_bytes(1048576), "1.00 MB")
        self.assertEqual(format_bytes(1073741824), "1.00 GB")
        self.assertEqual(format_bytes(-50), "0 B")

    def test_get_disk_usage(self):
        usage = get_disk_usage(".")
        self.assertIn("total_bytes", usage)
        self.assertIn("free_bytes", usage)
        self.assertIn("percent_used", usage)
        self.assertGreater(usage["total_bytes"], 0)


if __name__ == "__main__":
    unittest.main()
