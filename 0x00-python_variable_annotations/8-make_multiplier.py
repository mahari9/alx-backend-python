#!/usr/bin/env python3
"""Defines task 8's module."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a multiplier function."""
    return lambda x: x * multiplier
