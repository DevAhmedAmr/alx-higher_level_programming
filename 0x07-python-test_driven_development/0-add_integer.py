#!/usr/bin/python3
"""_summary_"""


def add_integer(a, b=98):
    """add_integer"""

    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    result = int(a) + int(b)

    return result
