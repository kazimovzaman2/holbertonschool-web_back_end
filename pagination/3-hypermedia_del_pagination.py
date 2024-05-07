#!/usr/bin/env python3
"""Python pagination module"""
import csv
from typing import Dict, List


index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate"""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server"""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Load dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Load indexed dataset"""
        if self.__indexed_dataset is None:
            self.__indexed_dataset = [
                (i, row) for i, row in enumerate(self.dataset())
            ]

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get hypermedia pagination with index"""
        assert 0 <= index < len(self.dataset())

        indexed_dataset = self.indexed_dataset()
        indexed_page = {}

        i = index
        while len(indexed_page) < page_size and i < len(self.dataset()):
            if i in indexed_dataset:
                indexed_page[i] = indexed_dataset[i]
            i += 1

        page = list(indexed_page.values())
        page_indices = indexed_page.keys()

        return {
            "index": index,
            "next_index": max(page_indices) + 1,
            "page_size": len(page),
            "data": page,
        }
