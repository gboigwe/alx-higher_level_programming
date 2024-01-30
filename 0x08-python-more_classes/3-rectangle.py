#!/usr/bin/python3
"""
This module defines a rectangle class
"""


class Rectangle:
    """
    Class Rectangle: A rectangle class
    __init__: initializes the class with private argument width and height
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

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

    def __str__(self):
        rect = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                rect += '#' * self.__width + '\n'
                
        return rect[:-1]

#    def __str__(self):
#        rect = ""
#        for i in range(self.__height):
#            rect += '#' * self.__width
#            if self.__width != 0 and i < (self.__height - 1):
#                rect += '\n'
#        return rect

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)


my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))
