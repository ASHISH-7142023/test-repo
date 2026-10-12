"""Unit tests for collection manipulation utilities."""

import unittest
from src.collection_utils import chunk_list, dedupe, flatten_dict, deep_merge


class TestCollectionUtils(unittest.TestCase):

    def test_chunk_list(self):
        items = [1, 2, 3, 4, 5, 6, 7]
        chunks = chunk_list(items, chunk_size=3)
        self.assertEqual(chunks, [[1, 2, 3], [4, 5, 6], [7]])

        with self.assertRaises(ValueError):
            chunk_list(items, 0)

    def test_dedupe(self):
        items = [4, 1, 2, 1, 3, 4, 2, 5]
        self.assertEqual(dedupe(items), [4, 1, 2, 3, 5])
        self.assertEqual(dedupe([]), [])

    def test_flatten_dict(self):
        nested = {
            "app": {
                "name": "DevToolkit",
                "settings": {"debug": True, "port": 8080}
            },
            "version": "1.0"
        }
        flat = flatten_dict(nested)
        self.assertEqual(flat, {
            "app.name": "DevToolkit",
            "app.settings.debug": True,
            "app.settings.port": 8080,
            "version": "1.0"
        })

    def test_deep_merge(self):
        d1 = {"a": 1, "nested": {"x": 10, "y": 20}}
        d2 = {"b": 2, "nested": {"y": 99, "z": 30}}
        merged = deep_merge(d1, d2)
        self.assertEqual(merged, {
            "a": 1,
            "b": 2,
            "nested": {"x": 10, "y": 99, "z": 30}
        })


if __name__ == "__main__":
    unittest.main()
