#!/usr/bin/env python3
"""Python annotation task"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums up all the elements in the input_list and returns the total.
    """
    n = 0
    for i in input_list:
        n += i

    return n
