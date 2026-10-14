"""Unit tests for dictionary difference and text unified diff helpers."""

import unittest
from src.diff_utils import diff_dicts, unified_diff_text


class TestDiffUtils(unittest.TestCase):

    def test_diff_dicts(self):
        old_data = {"a": 1, "b": 2, "c": 3}
        new_data = {"b": 20, "c": 3, "d": 4}
        res = diff_dicts(old_data, new_data)

        self.assertEqual(res["added"], {"d": 4})
        self.assertEqual(res["removed"], {"a": 1})
        self.assertEqual(res["modified"], {"b": (2, 20)})

    def test_unified_diff_text(self):
        text_a = "line 1\nline 2\nline 3\n"
        text_b = "line 1\nline 2 modified\nline 3\n"
        diff = unified_diff_text(text_a, text_b)
        self.assertIn("--- before", diff)
        self.assertIn("+++ after", diff)
        self.assertIn("-line 2", diff)
        self.assertIn("+line 2 modified", diff)


if __name__ == "__main__":
    unittest.main()
