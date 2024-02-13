#!/usr/bin/python3
"""
Rectangle - Created class that inherits Base class

Classes: Inherits from Base class

Initializes: width (int), height (int), x (int), y (int)
"""


from .base import Base


class Rectangle(Base):
    """Rectangle class created

    Inherits id from base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing all these arg instances

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
            """Check for the data type"""
            raise TypeError("width must be an integer")
        elif value <= 0:
            """Chcke if value is less than or equal to 0"""
            raise ValueError("width must be > 0")
        """Set the value"""
        self.__width = value
        """Initialize with the id"""

    @property
    def height(self):
        """Getting the private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the private instance height"""
        if not isinstance(value, int):
            """Check for the data type"""
            raise TypeError("height must be an integer")
        elif value <= 0:
            """Check if value is less than or equal to 0"""
            raise ValueError("height must be > 0")
        self.__height = value
        """Initialize with the id"""

    @property
    def x(self):
        """Getting the private instance x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting the private instance x"""
        if not isinstance(value, int):
            """Check for the data type"""
            raise TypeError("x must be an integer")
        elif value < 0:
            """Check if value is less than 0"""
            raise ValueError("x must be >= 0")
        self.__x = value
        """Initialize with the id"""

    @property
    def y(self):
        """Getting the private instance y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting the private instance y"""
        if not isinstance(value, int):
            """Check for the data type"""
            raise TypeError("y must be an integer")
        elif value < 0:
            """Check if value is less than 0"""
            raise ValueError("y must be >= 0")
        self.__y = value
        """Initialize with the id"""

    def area(self):
        """Calculating the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        pass
