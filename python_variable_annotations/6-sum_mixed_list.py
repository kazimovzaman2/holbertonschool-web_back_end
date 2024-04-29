#!/usr/bin/env python3
"""Python annotation task"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum of a list of integers and floats"""
    return sum(mxd_lst)
