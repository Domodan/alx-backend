#!/usr/bin/python3
"""
    Moduel: LRUCache caching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
        LRUCache provides an object that assigns to and retrieves items from a
        dictionary with a LRU removal mechanism
    """

    def __init__(self):
        """
            Initializes the cache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
            Puts item in cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            lru_key = self.get_first_list(self.queue)
            if lru_key:
                self.queue.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.mv_last_list(key)

    def get(self, key):
        """
            Gets an item from cache
        """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.mv_last_list(key)
        return item

    def mv_last_list(self, item):
        """
            Moves element to last idx of list
        """
        length = len(self.queue)
        if self.queue[length - 1] != item:
            self.queue.remove(item)
            self.queue.append(item)

    @staticmethod
    def get_first_list(array):
        """
            Get first element of list or None
        """
        return array[0] if array else None
