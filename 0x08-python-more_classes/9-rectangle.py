#!/usr/bin/python3
"""
This module defines a rectangle class
"""


class Rectangle:
    """
    Class Rectangle: A rectangle class
    __init__: initializes the class with private argument width and height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Class Rectangle: A rectangle class
        __init__: initializes the class with private argument width and height
        """

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Generates square instance with equal width and height.
        Args:
            cls: Access class attributes.
            size: Size of the square (one side). Defaults to 0.
        Returns:
            Square: New rectangle with equal width and height.
        """

        return Rectangle(size, size)

    def __str__(self):
        rect = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                rect += "{}".format(self.print_symbol) * self.__width + '\n'
        return rect[:-1]

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
