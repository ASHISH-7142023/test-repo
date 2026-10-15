"""Unit tests for offset and cursor pagination utilities."""

import unittest
from src.pagination_utils import paginate_list, cursor_paginate


class TestPaginationUtils(unittest.TestCase):

    def test_paginate_list_first_page(self):
        data = list(range(1, 26))
        p1 = paginate_list(data, page=1, per_page=10)
        self.assertEqual(p1.items, list(range(1, 11)))
        self.assertEqual(p1.total_pages, 3)
        self.assertTrue(p1.has_next)
        self.assertFalse(p1.has_prev)

    def test_paginate_list_last_page(self):
        data = list(range(1, 26))
        p3 = paginate_list(data, page=3, per_page=10)
        self.assertEqual(p3.items, list(range(21, 26)))
        self.assertFalse(p3.has_next)
        self.assertTrue(p3.has_prev)

    def test_cursor_paginate(self):
        items = [{"id": i, "val": f"val_{i}"} for i in range(1, 10)]
        res1 = cursor_paginate(items, cursor_key="id", limit=3)
        self.assertEqual(len(res1["items"]), 3)
        self.assertEqual(res1["next_cursor"], 3)
        self.assertTrue(res1["has_more"])

        res2 = cursor_paginate(items, cursor_key="id", cursor_val=res1["next_cursor"], limit=3)
        self.assertEqual(res2["items"][0]["id"], 4)


if __name__ == "__main__":
    unittest.main()
