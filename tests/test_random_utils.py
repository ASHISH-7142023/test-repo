"""Unit tests for random utilities."""

import random
import unittest
from src.random_utils import random_alphanumeric, weighted_choice, shuffle_copy, roll_dice


class TestRandomUtils(unittest.TestCase):

    def test_random_alphanumeric(self):
        s = random_alphanumeric(20)
        self.assertEqual(len(s), 20)
        self.assertTrue(s.isalnum())

    def test_weighted_choice_deterministic(self):
        random.seed(42)
        choices = {"common": 90.0, "rare": 10.0}
        pick = weighted_choice(choices)
        self.assertIn(pick, choices)

    def test_roll_dice(self):
        rolls = roll_dice(sides=6, count=5)
        self.assertEqual(len(rolls), 5)
        for r in rolls:
            self.assertTrue(1 <= r <= 6)


if __name__ == "__main__":
    unittest.main()
