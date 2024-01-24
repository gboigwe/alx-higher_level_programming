#!/usr/bin/python3
"""Creating Python Project by defining class Square
"""


class Square:
    """creating square class.

    Args:
    size (int): length of square considered

    Attributes:
    __size (int): length of square

    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """__size getter for setter

        Returns:
        __size (int): length of square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Args:
        value (int): length of square

        Attributes:
        __size (int): setters of square
        Raises:
        TypeError: if value is not an integer
        ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calulates area of square.
        Attributes:
        __size (int): length of square
        Returns: area (int): length of squared
        """
        area = self.__size * self.__size
        return area
