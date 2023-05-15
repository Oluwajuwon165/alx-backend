#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer arguments
page and page_size.

The function should return a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return in a
list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""

from typing import Tuple, List
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of start and end indices for a given page and page_size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self._dataset = None

    def dataset(self) -> List[List[str]]:
        """
        Returns the cached dataset
        """
        if self._dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self._dataset = [row for row in reader][1:]
        return self._dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Returns the appropriate page of the dataset
        """
        assert isinstance(page, int) and page > 0, "Invalid page number"
        assert isinstance(page_size, int) and page_size > 0, "Invalid page size"

        data = self.dataset()
        start, end = index_range(page, page_size)
        return data[start:end]
