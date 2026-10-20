import unittest
from src.text_diff_patch import create_unified_diff, apply_patch

class TestTextDiffPatch(unittest.TestCase):
    def test_diff_and_patch(self):
        orig = "line 1\nline 2\nline 3"
        mod = "line 1\nline TWO\nline 3"
        diff = create_unified_diff(orig, mod)
        patched = apply_patch(orig, diff)
        self.assertEqual(patched, mod)

if __name__ == "__main__":
    unittest.main()
