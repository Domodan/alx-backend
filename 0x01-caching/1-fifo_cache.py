#!/usr/bin/python3
"""
    Module: FIFOCache class inheriting from BaseCaching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        FIFOCache provides an object that allows storing and retrieving items
        from a dictionary with a FIFO removal mechanism
    """

    def __init__(self):
        """
            Initialize FIFOCache
        """
        self.queue = []
        super().__init__()

    def put(self, key, item):
        """
            Assign the item to the dictionary
        """
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete = self.queue.pop(0)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        """
            Output the value associated with the given key
        """
        return self.cache_data.get(key)
