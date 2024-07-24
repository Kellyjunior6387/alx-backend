#!/usr/bin/env python3
"""Module to implement the get and put methods"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
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
                self.add_key(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    first = self.order.pop(0)
                    del self.cache_data[first]
                    print(f"DISCARD: {first}")
                self.cache_data[key] = item
                self.order.append(key)

    def get(self, key):
        """Get the value matching the key
        """
        if key in self.cache_data.keys():
            self.add_key(key)
            return self.cache_data[key]
        else:
            return None

    def add_key(self, key):
        """ Method to track recently used key
        """
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)
