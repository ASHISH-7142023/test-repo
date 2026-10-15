"""Unit tests for ASCII and Markdown table formatters."""

import unittest
from src.table_utils import format_ascii_table, format_markdown_table


class TestTableUtils(unittest.TestCase):

    def test_format_ascii_table(self):
        headers = ["ID", "Name", "Role"]
        rows = [
            [1, "Alice", "Admin"],
            [2, "Bob", "User"]
        ]
        table = format_ascii_table(headers, rows)
        self.assertIn("Alice", table)
        self.assertIn("Admin", table)
        self.assertTrue(table.startswith("+"))
        self.assertTrue(table.endswith("+"))

    def test_format_markdown_table(self):
        headers = ["Module", "Status"]
        rows = [["Auth", "OK"], ["DB", "OK"]]
        md = format_markdown_table(headers, rows)
        self.assertIn("| Module | Status |", md)
        self.assertIn("| --- | --- |", md)
        self.assertIn("| Auth | OK |", md)


if __name__ == "__main__":
    unittest.main()
