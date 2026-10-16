"""Unit tests for MarkdownBuilder."""

import unittest
from src.markdown_builder import MarkdownBuilder


class TestMarkdownBuilder(unittest.TestCase):

    def test_markdown_generation(self):
        mb = MarkdownBuilder()
        doc = (mb.header("Project Title", level=1)
               .paragraph("Welcome to the project.")
               .bullet_list(["Feature 1", "Feature 2"])
               .build())

        self.assertIn("# Project Title", doc)
        self.assertIn("Welcome to the project.", doc)
        self.assertIn("- Feature 1", doc)


if __name__ == "__main__":
    unittest.main()
