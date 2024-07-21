#!/usr/bin/env python3
"""Module to create a helper function"""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int]:
    """ Function to  to return in a list for pagination parameters.
    param page: start of the page
    param page_size: the size of a page
    """
    
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
