#!/usr/bin/env python3
"""Cache memory management."""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    def put(self, key, item):
        pass

    def get(self, key):
        """Return the value associated with the provided key."""
        for k,v in self.cache_data.items():
            if k == key:
                return v
        return None
