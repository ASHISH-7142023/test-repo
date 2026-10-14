"""Unit tests for regular expression entity extraction helpers."""

import unittest
from src.regex_patterns import (
    extract_emails,
    extract_urls,
    extract_hashtags,
    extract_mentions,
    extract_ipv4_addresses
)


class TestRegexPatterns(unittest.TestCase):

    def test_extract_emails(self):
        text = "Contact us at support@example.com or sales.dept+tag@work.org."
        emails = extract_emails(text)
        self.assertEqual(emails, ["support@example.com", "sales.dept+tag@work.org"])

    def test_extract_urls(self):
        text = "Visit https://github.com and http://example.com/api?q=1 today!"
        urls = extract_urls(text)
        self.assertEqual(len(urls), 2)
        self.assertTrue(urls[0].startswith("https://github.com"))

    def test_extract_hashtags_and_mentions(self):
        text = "Loving the new #python update! Kudos to @octocat and #devcommunity."
        self.assertEqual(extract_hashtags(text), ["python", "devcommunity"])
        self.assertEqual(extract_mentions(text), ["octocat"])

    def test_extract_ipv4(self):
        text = "Host server connected from 192.168.1.10 to 10.0.0.1 on port 80."
        self.assertEqual(extract_ipv4_addresses(text), ["192.168.1.10", "10.0.0.1"])


if __name__ == "__main__":
    unittest.main()
