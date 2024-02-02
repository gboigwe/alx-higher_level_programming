#!/usr/bin/python3
"""Defines argument integer function"""


def add_integer(a, b=98):
    """
    Defines the addition of variable a and b

    Args:
    a: Holds first variable
    b: Holds second variable

    Raise:
        TypeError: if either a orb is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
