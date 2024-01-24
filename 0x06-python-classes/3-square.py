#!/usr/bin/python3
"""Creating square module for Python
"""


class Square:
    """Defining class square

    Args:
    size (int): length of square considered

    Attributes:
    __size (int): length of square considered

    Raises:
    TypeError: Error for non integer
    ValueError: Error for less than 0

    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Defining area of square.

        Attributes:
        __size (int): length of square considered

        Returns:
        area (int): Result of area returned

        """
        area = self.__size * self.__size
        return area
