#!/usr/bin/python3
"""
Module for adding integers.


"""


def add_integer(a, b=98):
    """
    Returns the sum of or adds two integers.
    """

    """
    if not isinstance(a, (int, float)) and not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
