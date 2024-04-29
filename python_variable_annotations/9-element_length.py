#!/usr/bin/env python3
"""Python annotation task"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples of a sequence and its length"""
    return [(i, len(i)) for i in lst]
