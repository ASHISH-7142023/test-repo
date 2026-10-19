"""
LFU Cache (Least Frequently Used) with O(1) operations.
Zero external dependencies.
"""
from typing import TypeVar, Generic, Dict, Optional
from collections import OrderedDict

K = TypeVar("K")
V = TypeVar("V")

class LFUCache(Generic[K, V]):
    """
    O(1) LFU Cache implementation using frequency buckets with OrderedDict.
    """
    def __init__(self, capacity: int):
        if capacity < 0:
            raise ValueError("capacity must be >= 0")
        self.capacity = capacity
        self.key_to_val: Dict[K, V] = {}
        self.key_to_freq: Dict[K, int] = {}
        self.freq_to_keys: Dict[int, OrderedDict] = {}
        self.min_freq: int = 0

    def __len__(self) -> int:
        return len(self.key_to_val)

    def __contains__(self, key: K) -> bool:
        return key in self.key_to_val

    def _update_freq(self, key: K) -> None:
        freq = self.key_to_freq[key]
        self.key_to_freq[key] = freq + 1
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        new_freq = freq + 1
        if new_freq not in self.freq_to_keys:
            self.freq_to_keys[new_freq] = OrderedDict()
        self.freq_to_keys[new_freq][key] = None

    def get(self, key: K, default: Optional[V] = None) -> Optional[V]:
        if key not in self.key_to_val:
            return default
        self._update_freq(key)
        return self.key_to_val[key]

    def put(self, key: K, value: V) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._update_freq(key)
            return

        if len(self.key_to_val) >= self.capacity:
            evict_keys = self.freq_to_keys[self.min_freq]
            evict_key, _ = evict_keys.popitem(last=False)
            if not evict_keys:
                del self.freq_to_keys[self.min_freq]
            del self.key_to_val[evict_key]
            del self.key_to_freq[evict_key]

        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.min_freq = 1
        if 1 not in self.freq_to_keys:
            self.freq_to_keys[1] = OrderedDict()
        self.freq_to_keys[1][key] = None

    def delete(self, key: K) -> bool:
        if key not in self.key_to_val:
            return False
        freq = self.key_to_freq[key]
        del self.key_to_val[key]
        del self.key_to_freq[key]
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq = min(self.freq_to_keys.keys()) if self.freq_to_keys else 0
        return True

    def clear(self) -> None:
        self.key_to_val.clear()
        self.key_to_freq.clear()
        self.freq_to_keys.clear()
        self.min_freq = 0
