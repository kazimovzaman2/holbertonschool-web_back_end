#!/usr/bin/env python3
"""Python annotation task"""
from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """Returns a tuple of a string and a number squared"""
    return (k, v ** 2)
