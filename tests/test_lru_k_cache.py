import unittest
from src.lru_k_cache import LRUKCache

class TestLRUKCache(unittest.TestCase):
    def test_capacity_and_eviction(self):
        cache = LRUKCache(capacity=2, k=2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.get("a")
        cache.put("c", 3)
        self.assertIn("a", cache.data)
        self.assertIn("c", cache.data)
        self.assertNotIn("b", cache.data)

    def test_delete_and_clear(self):
        cache = LRUKCache(2)
        cache.put("x", 10)
        self.assertTrue(cache.delete("x"))
        self.assertFalse(cache.delete("y"))
        self.assertEqual(len(cache), 0)

if __name__ == "__main__":
    unittest.main()
