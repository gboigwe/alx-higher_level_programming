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

    def __ge__(self, other):
        self.area() >= other.area()

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Class Rectangle: A rectangle class
        __init__: initializes the class with private argument width and height
        """
        greater_rect_1 = rect_1.area() >= rect_2.area()
        greater_rect_2 = rect_2.area() >= rect_1.area()
        
        if greater_rect_1 is True:
            try:
                pass
            except:
                raise TypeError("rect_1 must be an instance of Rectangle")
            return rect_1
        elif greater_rect_2 is True:
            try:
                pass
            except:
                raise TypeError("rect_2 must be an instance of Rectangle")
            return rect_2
        else:
            return rect_1
#        try:
#            rect_1.area() >= rect_2.area()
#        except:
#            raise TypeError("rect_1 must be an instance of Rectangle")
#        try:
#            rect_2.area() >= rect_1.area()
#        except:
#            raise TypeError("rect_2 must be an instance of Rectangle")
#        if rect_1.area() == rect_2.area():
#            return rect_1
#        greater_rect_1 = rect_1.area() >= rect_2.area()
#        greater_rect_2 = rect_2.area() >= rect_1.area()
#        if greater_rect_1 is True:
#            return rect_1.area()
#        else:
#            raise TypeError("rect_1 must be an instance of Rectangle")
#        if greater_rect_2 is True:
#            return rect_2.area()
#        else:
#            raise TypeError("rect_2 must be an instance of Rectangle")
#        return rect_1.area()


my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")
