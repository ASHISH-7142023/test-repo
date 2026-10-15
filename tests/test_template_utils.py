"""Unit tests for string template interpolation."""

import unittest
from src.template_utils import render_template


class TestTemplateUtils(unittest.TestCase):

    def test_render_template(self):
        tmpl = "Hello, {{ name }}! You have {{ count }} notifications."
        out = render_template(tmpl, {"name": "Ashish", "count": 5})
        self.assertEqual(out, "Hello, Ashish! You have 5 notifications.")

    def test_render_template_missing_key_fallback(self):
        tmpl = "Status: {{ status }}, Code: {{ code }}"
        out = render_template(tmpl, {"status": "Active"}, default="N/A")
        self.assertEqual(out, "Status: Active, Code: N/A")


if __name__ == "__main__":
    unittest.main()
