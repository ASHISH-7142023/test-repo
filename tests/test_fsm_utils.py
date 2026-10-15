"""Unit tests for Finite State Machine engine."""

import unittest
from src.fsm_utils import StateMachine


class TestFSMUtils(unittest.TestCase):

    def test_state_transitions(self):
        fsm = StateMachine(initial_state="draft")
        fsm.add_transition("draft", "submit", "pending_review")
        fsm.add_transition("pending_review", "approve", "published")

        self.assertEqual(fsm.trigger("submit"), "pending_review")
        self.assertEqual(fsm.trigger("approve"), "published")

    def test_invalid_transition_raises_error(self):
        fsm = StateMachine(initial_state="draft")
        with self.assertRaises(ValueError):
            fsm.trigger("approve")


if __name__ == "__main__":
    unittest.main()
