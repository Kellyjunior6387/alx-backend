#!/usr/bin/env python3
"""module to read a csv file"""
from math import ceil
import csv
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int]:
    """ Function to  to return in a list for pagination parameters.
    param page: start of the page
    param page_size: the size of a page
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get the cached pages
        """
        self.dataset()
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        if start > len(self.__dataset):
            return []
        return self.__dataset[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """Function to  to return in a list for pagination parameters.
            param page: start of the page
            param page_size: the size of a page
        """
        pagination = self.get_page(page, page_size)
        total = ceil(len(self.__dataset) / page_size)
        return {
            "page_size": len(pagination),
            "page": page,
            "data": pagination,
            "next_page": page + 1 if page < total else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total
        }
