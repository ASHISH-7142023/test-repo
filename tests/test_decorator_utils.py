"""Unit tests for functional decorators."""

import unittest
import warnings
from src.decorator_utils import memoize, deprecated, once


class TestDecoratorUtils(unittest.TestCase):

    def test_memoize_caches_result(self):
        call_count = 0

        @memoize
        def add(a, b):
            nonlocal call_count
            call_count += 1
            return a + b

        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(call_count, 1)

        self.assertEqual(add(4, 5), 9)
        self.assertEqual(call_count, 2)

        add.clear_cache()
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(call_count, 3)

    def test_deprecated_warning(self):
        @deprecated("Use new_function instead")
        def old_function():
            return "legacy"

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            val = old_function()
            self.assertEqual(val, "legacy")
            self.assertEqual(len(w), 1)
            self.assertTrue(issubclass(w[-1].category, DeprecationWarning))
            self.assertIn("Use new_function instead", str(w[-1].message))

    def test_once_decorator(self):
        runs = 0

        @once
        def initialize():
            nonlocal runs
            runs += 1
            return "init_done"

        self.assertEqual(initialize(), "init_done")
        self.assertEqual(initialize(), "init_done")
        self.assertEqual(initialize(), "init_done")
        self.assertEqual(runs, 1)


if __name__ == "__main__":
    unittest.main()
