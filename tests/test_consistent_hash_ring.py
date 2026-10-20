import unittest
from src.consistent_hash_ring import ConsistentHashRing

class TestConsistentHashRing(unittest.TestCase):
    def test_routing(self):
        ring = ConsistentHashRing(["nodeA", "nodeB", "nodeC"], replicas=50)
        n1 = ring.get_node("user_123")
        self.assertIn(n1, ["nodeA", "nodeB", "nodeC"])
        ring.remove_node(n1)
        n2 = ring.get_node("user_123")
        self.assertNotEqual(n1, n2)

if __name__ == "__main__":
    unittest.main()
