#!/usr/bin/python3
"""
Defines a function that prints Square module with "#".

useful for all square-based applications
"""


def print_square(size):
    """
    using size of length of the square
    size must be an integer
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for x in range(size):
        print('#' * size)
9