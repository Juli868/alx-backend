#!/usr/bin/env python3
"""Cache memory management."""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Utilise FIFO algoritm."""

    def put(self, key, item):
        """Add a new cache data to the dictionary."""
        if key is not None or item is not None:
            length = len(self.cache_data)
            if (length == BaseCaching.MAX_ITEMS):
                first_key, first_value = next(iter(self.cache_data.items()))
                print(f'DISCARD: {first_key}\n')
                del self.cache_data[first_key]
            self.cache_data[key] = item
        return

    def get(self, key):
        """Return the value associated with the provided key."""
        for k,v in self.cache_data.items():
            if k == key:
                return v
        return None
