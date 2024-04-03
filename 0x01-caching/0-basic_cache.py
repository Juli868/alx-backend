#!/usr/bin/env python3
"""Cache memory management."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """."""

    def put(self, key, item):
        """Define the data dictionary."""
        if (key is not None or item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """Return the data for the provided key."""
        for k, v  in self.cache_data.items():
            if k == key:
                return v
        return None
