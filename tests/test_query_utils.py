"""Unit tests for query string manipulation helpers."""

import unittest
from src.query_utils import parse_query_params, build_query_string, filter_query_params


class TestQueryUtils(unittest.TestCase):

    def test_parse_query_params(self):
        qs = "?search=python&page=2&tag=dev&tag=tools"
        params = parse_query_params(qs)
        self.assertEqual(params["search"], "python")
        self.assertEqual(params["page"], "2")
        self.assertEqual(params["tag"], ["dev", "tools"])

    def test_build_query_string(self):
        params = {"b": 2, "a": 1, "c": None}
        out = build_query_string(params, sort_keys=True)
        self.assertEqual(out, "a=1&b=2")

    def test_filter_query_params(self):
        qs = "user=admin&token=secret&debug=1"
        filtered = filter_query_params(qs, ["user", "debug"])
        self.assertIn("user=admin", filtered)
        self.assertIn("debug=1", filtered)
        self.assertNotIn("token", filtered)


if __name__ == "__main__":
    unittest.main()
