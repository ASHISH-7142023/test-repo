"""Unit tests for thread-safe EventBus publish-subscribe pattern."""

import unittest
from src.event_bus import EventBus


class TestEventBus(unittest.TestCase):

    def test_subscribe_and_publish(self):
        bus = EventBus()
        received = []

        def on_user_signup(user_id, email):
            received.append((user_id, email))

        bus.subscribe("user.signup", on_user_signup)
        dispatched = bus.publish("user.signup", 101, "dev@example.com")

        self.assertEqual(dispatched, 1)
        self.assertEqual(received, [(101, "dev@example.com")])

    def test_unsubscribe(self):
        bus = EventBus()
        calls = 0

        def handler():
            nonlocal calls
            calls += 1

        bus.subscribe("ping", handler)
        bus.publish("ping")
        self.assertEqual(calls, 1)

        self.assertTrue(bus.unsubscribe("ping", handler))
        bus.publish("ping")
        self.assertEqual(calls, 1)

    def test_clear_all_handlers(self):
        bus = EventBus()
        bus.subscribe("e1", lambda: None)
        bus.subscribe("e2", lambda: None)
        bus.clear()
        self.assertEqual(bus.publish("e1"), 0)
        self.assertEqual(bus.publish("e2"), 0)


if __name__ == "__main__":
    unittest.main()
