#!/usr/bin/python3
"""A module that defines a Rectangle creating class `Rectangle`

Classes:
    -Rectangle:
    Initializes: width (int), height (int), x (int), y (int)
"""


from .base import Base


class Rectangle(Base):
    """
    Rectangle class created
    Inherits id from base class

    Args:
        @Base: Superclass, inherited from

    Methods:
        -__init__: initializes an instance of a Recangle
            *defaults x=0, y=0 and id to None
        - area: returns the area of the Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializing all these arg instances
        Args:
            width (int), height (int), x (int), y (int)
        Inherits id from Base class
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getting the private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the private instance width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getting the private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the private instance height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getting the private instance x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting the private instance x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getting the private instance y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting the private instance y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculating the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """Defining a public method that prints in stdout"""
        for y in range(self.__y):
            print("")
        for he in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for w in range(self.__width)]
            print("")

    def __str__(self):
        """Overiding str method to return a designed output"""
        return str("[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Updating rectangle with args and kwargs"""
        if args is not None and len(args) > 0:
            keylist = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, keylist[i], args[i])
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
