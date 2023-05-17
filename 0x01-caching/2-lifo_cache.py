#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            if key not in self.cache_data:
                discarded_key = self.keys.pop()
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
