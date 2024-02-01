#!/usr/bin/python3
"""Defines arg integer function"""


def add_integer(a, b=98):
    """Returns the addition of variable a and b

    Args:
        Variables must be int and float

    Raise:
        TypeError: if either a orb is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
