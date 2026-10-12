"""Unit tests for string utilities."""

import unittest
from src.string_utils import slugify, camel_to_snake, snake_to_camel, truncate_words, mask_sensitive


class TestStringUtils(unittest.TestCase):

    def test_slugify(self):
        self.assertEqual(slugify("Hello World! 2026"), "hello-world-2026")
        self.assertEqual(slugify("Café & Restaurant"), "cafe-restaurant")
        self.assertEqual(slugify(""), "")

    def test_camel_to_snake(self):
        self.assertEqual(camel_to_snake("camelCaseString"), "camel_case_string")
        self.assertEqual(camel_to_snake("PascalCaseString"), "pascal_case_string")
        self.assertEqual(camel_to_snake("simple"), "simple")
        self.assertEqual(camel_to_snake(""), "")

    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel("hello_world"), "helloWorld")
        self.assertEqual(snake_to_camel("hello_world", pascal=True), "HelloWorld")
        self.assertEqual(snake_to_camel(""), "")

    def test_truncate_words(self):
        text = "The quick brown fox jumps over the lazy dog near the river"
        self.assertEqual(truncate_words(text, max_words=5), "The quick brown fox jumps...")
        self.assertEqual(truncate_words("Short text", max_words=10), "Short text")
        self.assertEqual(truncate_words(""), "")

    def test_mask_sensitive(self):
        self.assertEqual(mask_sensitive("1234567812345678", visible_chars=4), "************5678")
        self.assertEqual(mask_sensitive("secret_api_key_abc", visible_chars=3, mask_char="#"), "###############abc")
        self.assertEqual(mask_sensitive("short", visible_chars=10), "short")


if __name__ == "__main__":
    unittest.main()
