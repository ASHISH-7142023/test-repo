"""Unit tests for fluent URLBuilder."""

import unittest
from src.url_builder import URLBuilder


class TestURLBuilder(unittest.TestCase):

    def test_fluent_builder(self):
        url = (URLBuilder()
               .set_scheme("https")
               .set_host("api.github.com")
               .add_path("repos", "owner", "repo")
               .add_param("page", 1)
               .build())
        self.assertEqual(url, "https://api.github.com/repos/owner/repo?page=1")

    def test_parse_existing_base(self):
        builder = URLBuilder("http://example.com:8080/v1")
        builder.add_path("users").add_param("active", "true")
        self.assertEqual(builder.build(), "http://example.com:8080/v1/users?active=true")


if __name__ == "__main__":
    unittest.main()
