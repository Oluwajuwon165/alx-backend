#!/usr/bin/env python3
"""
LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.usage_count = {}
        self.frequency = {}

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            min_frequency = min(self.frequency.values())
            keys_to_discard = [
                k for k in self.frequency if self.frequency[k] == min_frequency
            ]
            least_recently_used = min(
                keys_to_discard, key=self.usage_count.get
            )
            del self.cache_data[least_recently_used]
            del self.usage_count[least_recently_used]
            del self.frequency[least_recently_used]
            print("DISCARD:", least_recently_used)

        self.cache_data[key] = item
        self.usage_count[key] = 0
        self.frequency[key] = 0

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        self.usage_count[key] += 1
        self.frequency[key] += 1
        return self.cache_data[key]
