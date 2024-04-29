#!/usr/bin/env python3
"""Python annotation task"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiply a float by a multiplier"""
    def multiply(num: float) -> float:
        """Multiply a float by a multiplier"""
        return num * multiplier
    return multiply
