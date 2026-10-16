"""Unit tests for consistent HashRing utilities."""

import unittest
from src.hash_ring import HashRing


class TestHashRing(unittest.TestCase):

    def test_add_and_get_node(self):
        hr = HashRing(replicas=50)
        hr.add_node("server-1")
        hr.add_node("server-2")

        n1 = hr.get_node("user_1001")
        n2 = hr.get_node("user_1002")
        self.assertIn(n1, ["server-1", "server-2"])
        self.assertIn(n2, ["server-1", "server-2"])

    def test_deterministic_key_placement(self):
        hr = HashRing(replicas=50)
        hr.add_node("node-a")
        hr.add_node("node-b")
        first_pick = hr.get_node("session_xyz")
        for _ in range(10):
            self.assertEqual(hr.get_node("session_xyz"), first_pick)

    def test_remove_node(self):
        hr = HashRing(replicas=20)
        hr.add_node("node-1")
        self.assertEqual(hr.get_node("test_key"), "node-1")
        hr.remove_node("node-1")
        self.assertIsNone(hr.get_node("test_key"))


if __name__ == "__main__":
    unittest.main()
