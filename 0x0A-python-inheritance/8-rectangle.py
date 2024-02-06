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
    def __init__(self, width, height):
        BaseGeometry.__init__(self)
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
