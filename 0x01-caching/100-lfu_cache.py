#!/usr/bin/python3
"""
    Moduele: LFUCache - Least Frequently Used caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
        LFUCache provides an object that assigns and retrieves items from a
        dictionary with a LFU removal mechanism
    """

    def __init__(self):
        """
            Initializes the cache
        """
        super().__init__()
        self.queue = []
        self.counter = {}

    def put(self, key, item):
        """
            Adds an item in cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        item_count = self.counter.get(key, None)

        if item_count is not None:
            self.counter[key] += 1
        else:
            self.counter[key] = 1

        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            lfu_key = self.get_first_list(self.queue)
            if lfu_key:
                self.queue.pop(0)
                del self.cache_data[lfu_key]
                del self.counter[lfu_key]
                print("DISCARD: {}".format(lfu_key))

        if key not in self.queue:
            self.queue.insert(0, key)
        self.mv_right_list(key)

    def get(self, key):
        """
            Gets an item from cache
        """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.counter[key] += 1
            self.mv_right_list(key)
        return item

    def mv_right_list(self, item):
        """
            Moves element to the right, taking into account LFU
        """
        length = len(self.queue)

        idx = self.queue.index(item)
        item_count = self.counter[item]

        for i in range(idx, length):
            if i != (length - 1):
                nxt = self.queue[i + 1]
                nxt_count = self.counter[nxt]

                if nxt_count > item_count:
                    break

        self.queue.insert(i + 1, item)
        self.queue.remove(item)

    @staticmethod
    def get_first_list(array):
        """
            Get first element of list or None
        """
        return array[0] if array else None