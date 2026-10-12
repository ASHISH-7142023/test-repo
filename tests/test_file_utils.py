"""Unit tests for file system utilities."""

import os
import shutil
import tempfile
import unittest
from src.file_utils import ensure_directory, safe_read_json, atomic_write_text, get_file_checksum


class TestFileUtils(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_ensure_directory(self):
        nested = os.path.join(self.test_dir, "a", "b", "c")
        self.assertFalse(os.path.exists(nested))
        res = ensure_directory(nested)
        self.assertEqual(res, nested)
        self.assertTrue(os.path.isdir(nested))

    def test_atomic_write_and_checksum(self):
        target = os.path.join(self.test_dir, "test.txt")
        content = "Hello, DevToolkit file hashing!"
        atomic_write_text(target, content)

        self.assertTrue(os.path.exists(target))
        with open(target, "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), content)

        checksum = get_file_checksum(target)
        self.assertEqual(len(checksum), 64)

    def test_safe_read_json(self):
        missing = os.path.join(self.test_dir, "missing.json")
        self.assertEqual(safe_read_json(missing, default={"key": "val"}), {"key": "val"})

        valid_file = os.path.join(self.test_dir, "valid.json")
        atomic_write_text(valid_file, '{"success": true, "count": 42}')
        data = safe_read_json(valid_file)
        self.assertEqual(data, {"success": True, "count": 42})


if __name__ == "__main__":
    unittest.main()
