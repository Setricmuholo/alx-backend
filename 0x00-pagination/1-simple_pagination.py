#!/usr/bin/env python3
"""
a defination of the index_range function
"""

from typing import Tuple
import csv
import math
from typing import List

def index_range(page: int, page_size: int):

    """
    The function should return a tuple of size two containing a start index and an end index corresponding
    to the range of indexes to return in a list for those particular pagination parameters.
    Page numbers are 1-indexed, i.e. the first page is page 1.
    """

    start, end = 0, 0
    for i in range(page):
        start = end
        end = end + page_size

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
    """
    takes two integer arguments page with default value 1 and page_size with default value 10.
    Use assert to verify that both arguments are integers greater than 0.
    Use index_range to find the correct indexes to paginate the dataset,
    correctly and return the appropriate page of the dataset (i.e. the correct list of rows).
    If the input arguments are out of range for the dataset, an empty list should be returned.
    """
    assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()
        data_length = len(dataset)
        try:
            index = index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []
