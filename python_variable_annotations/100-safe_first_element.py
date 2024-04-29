#!/usr/bin/env python3
"""Python annotation task"""
from typing import Sequence, Optional, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Returns the first element of a sequence or None"""
    if lst:
        return lst[0]
    else:
        return None
