#!/usr/bin/python3
"""
Defines argument integer function
it adds 2 integers
a and b must be first casted
"""


def add_integer(a, b=98):
    """
    Defines the addition of variable a and b

    Args:
    a: Holds first variable
    b: Holds second variable

    Raise:
        TypeError: if either a orb is not an integer or float
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not (isinstance(a, int)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int)):
        raise TypeError("b must be an integer")
    return (a + b)
