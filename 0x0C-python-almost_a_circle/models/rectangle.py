#!/usr/bin/python3
"""Creating a class Rectangle that inherits from Base class
"""


from .base import Base


class Rectangle(Base):
    """Rectangle class created

    Inherits id from base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing all these arg instances

        Args:
            width (int), height (int), x (int), y (int)

        Inherits id from Base class
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def height(self):
        """Getting the instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the instance height"""
        self.__height = value

    @property
    def width(self):
        """Getting the instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the instance width"""
        self.__width = value

    @property
    def x(self):
        """Getting the instance x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting the instance x"""
        self.__x = value

    @property
    def y(self):
        """Getting the instance y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting the instance y"""
        self.__y = value
