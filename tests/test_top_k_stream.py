"""Unit tests for TopKStream tracker."""

import unittest
from src.top_k_stream import TopKStream


class TestTopKStream(unittest.TestCase):

    def test_top_k_ordering(self):
        tk = TopKStream(k=3)
        tk.add("low", score=10.0)
        tk.add("medium", score=50.0)
        tk.add("high", score=100.0)
        tk.add("super", score=200.0)

        top = tk.get_top_k()
        self.assertEqual(top, ["super", "high", "medium"])


if __name__ == "__main__":
    unittest.main()
