"""Unit tests for TTL and LRU in-memory caches."""

import time
import unittest
from src.cache_utils import TTLCache, LRUCache


class TestCacheUtils(unittest.TestCase):

    def test_ttl_cache_basic_and_expiration(self):
        cache = TTLCache(default_ttl_seconds=0.05)
        cache.set("short_key", "value_1")
        self.assertEqual(cache.get("short_key"), "value_1")

        # Wait for expiration
        time.sleep(0.06)
        self.assertIsNone(cache.get("short_key"))
        self.assertEqual(cache.get("short_key", default="fallback"), "fallback")

    def test_ttl_cache_delete_and_clear(self):
        cache = TTLCache(default_ttl_seconds=10.0)
        cache.set("k1", "v1")
        cache.set("k2", "v2")
        self.assertTrue(cache.delete("k1"))
        self.assertFalse(cache.delete("k1"))
        self.assertEqual(cache.size(), 1)
        cache.clear()
        self.assertEqual(cache.size(), 0)

    def test_lru_cache_eviction(self):
        cache = LRUCache(maxsize=3)
        cache.set("a", 1)
        cache.set("b", 2)
        cache.set("c", 3)

        # Access 'a' to make it recently used: order is now b, c, a
        self.assertEqual(cache.get("a"), 1)

        # Adding 'd' should evict 'b' (oldest)
        cache.set("d", 4)
        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.get("a"), 1)
        self.assertEqual(cache.get("c"), 3)
        self.assertEqual(cache.get("d"), 4)

    def test_lru_cache_delete_and_len(self):
        cache = LRUCache(maxsize=2)
        cache.set("x", 10)
        self.assertEqual(len(cache), 1)
        self.assertTrue(cache.delete("x"))
        self.assertEqual(len(cache), 0)


if __name__ == "__main__":
    unittest.main()
