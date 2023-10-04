#!/usr/bin/python3
"""_summary_"""


def add_integer(a, b=98):
    """add_integer"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if ((type(a) is float and a > 1.7976931348623157e+308) or
            (type(b) is float and b > 1.7976931348623157e+308)):
        raise OverflowError("cannot convert float infinity to integer")

    result = int(a) + int(b)
    
    if result == float('inf') or result == -float('inf'):
        raise OverflowError("float overflow")
    return result
