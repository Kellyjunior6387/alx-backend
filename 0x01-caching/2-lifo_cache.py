#!/usr/bin/env python3
"""Module to implement the get and put methods"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """inherits for BaseCaching and implement put and get
    """
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Assign to item to key in cached_data
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order.append(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    last = self.order.pop()
                    del self.cache_data[last]
                    print(f"DISCARD: {last}")
                self.cache_data[key] = item
                self.order.append(key)

    def get(self, key):
        """Get the value matching the key
        """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
