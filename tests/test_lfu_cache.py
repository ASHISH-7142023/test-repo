import unittest
from src.lfu_cache import LFUCache

class TestLFUCache(unittest.TestCase):
    def test_lfu_eviction(self):
        cache = LFUCache(capacity=2)
        cache.put("a", 1)
        cache.put("b", 2)
        self.assertEqual(cache.get("a"), 1)
        cache.put("c", 3)
        self.assertIn("a", cache)
        self.assertNotIn("b", cache)
        self.assertIn("c", cache)

    def test_deletion_and_clear(self):
        cache = LFUCache(capacity=3)
        cache.put(1, "one")
        cache.put(2, "two")
        self.assertTrue(cache.delete(1))
        self.assertFalse(cache.delete(99))
        self.assertEqual(len(cache), 1)
        cache.clear()
        self.assertEqual(len(cache), 0)

if __name__ == "__main__":
    unittest.main()
