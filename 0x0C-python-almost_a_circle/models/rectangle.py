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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        super().__init__(id)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
        super().__init__(id)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
        super().__init__(id)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        super().__init__(id)

    def area(self):
        return self.__width * self.__height

    def display(self):
        pass
