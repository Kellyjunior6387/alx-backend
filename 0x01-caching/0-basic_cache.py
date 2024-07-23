#!/usr/bin/env python3
"""Module to implement the get and put methods"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherits for BaseCaching and implement put and get
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Assign to item to key in cached_data
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get the value matching the key
        """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
