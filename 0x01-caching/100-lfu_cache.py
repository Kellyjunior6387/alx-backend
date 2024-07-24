#!/usr/bin/env python3
"""Module to implement the get and put methods"""
from base_caching import BaseCaching
from collections import Counter


class LFUCache(BaseCaching):
    """inherits for BaseCaching and implement put and get
    """
    def __init__(self):
        super().__init__()
        self.order = []
        self.counter = Counter()

    def put(self, key, item):
        """ Assign to item to key in cached_data
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    value = self.least_frequent()
                    del self.cache_data[value]
                    del self.counter[value]
                    self.order.remove(value)
                    print(f"DISCARD: {value}")
                self.cache_data[key] = item
            self.add_order(key)
            self.counter[key] += 1

    def get(self, key):
        """Get the value matching the key
        """
        if key is None or key not in self.cache_data:
            return None
        self.add_order(key)
        self.counter[key] += 1
        return self.cache_data[key]

    def add_order(self, key):
        """ Method to track recently used key
        """
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

    def least_frequent(self):
        """Return the least frequently used key
        """
        least = min(self.counter.values())
        least_values = [value for value, freq in self.counter.items()
                        if freq == least]
        for key in self.order:
            if key in least_values:
                return key
