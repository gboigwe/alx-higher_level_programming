#!/usr/bin/python3
"""
Defining a Base Geometry class
    Defining an empty area
    Validating an Integer
Creating a new Rectangle class
    Inherits from Base Geometry class
"""


class BaseGeometry:
    """Defining a Base Geometry class
    Initializing and validating integers

    Args:
        name: The name string to be considered
        value: The integer value to be considered
    """

    def __init__(self):
        """Initializaion is gets called as class
        start action
        """

        pass

    def area(self):
        """Defines a function for area of a geometry
        This function is not defined and can't be used

        It raises an error message to the developer to
        define it before use
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer

        Args:
            name: name is assumed to be string
            value: checking if type is an integer

        Raises error if value type is not integer
        Raises error if value is <= 0
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Defining a Rectangle class
    Initializing and inheriting BaseGeometry class

    Args:
        width: The value of the width is passed in
        height: The value of the height is passed in
    """

    def __init__(self, width, height):
        """Initializaion is called on the class
            width is initialized
            height is initialized
        """

        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Defines an area for the rectangle"""
        return self.__width * self.__height
