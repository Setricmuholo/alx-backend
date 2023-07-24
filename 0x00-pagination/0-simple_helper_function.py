#!/usr/bin/env python3
"""
a defination of the index_range function
"""

from typing import Tuple


def index_range(page: int, page_size: int):

    """
    The function should return a tuple of size two containing a start index
    """

    start, end = 0, 0
    for i in range(page):
        start = end
        end = end + page_size

    return (start, end)
