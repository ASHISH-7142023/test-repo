"""Unit tests for advanced slugification with stop-word removal."""

import unittest
from src.slug_enhancements import advanced_slugify


class TestSlugEnhancements(unittest.TestCase):

    def test_advanced_slugify_removes_stopwords(self):
        title = "The Quick Brown Fox and A Lazy Dog"
        slug = advanced_slugify(title, remove_stopwords=True)
        self.assertEqual(slug, "quick-brown-fox-lazy-dog")

    def test_advanced_slugify_keeps_stopwords_when_flag_false(self):
        title = "The Quick Fox"
        slug = advanced_slugify(title, remove_stopwords=False)
        self.assertEqual(slug, "the-quick-fox")


if __name__ == "__main__":
    unittest.main()
