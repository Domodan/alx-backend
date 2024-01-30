#!/usr/bin/env python3
"""
    Module: Basic caching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        Moduel to assign and retrieves from a dictionary
    """
    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key from cache.
        """
        return self.cache_data.get(key, None)
