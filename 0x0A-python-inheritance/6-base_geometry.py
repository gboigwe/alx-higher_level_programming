#!/usr/bin/python3
"""Defining an empty class"""


class BaseGeometry:
    """The class is empty and would pass afterwards"""

    def __init__(self):
        """Initializes an empty function"""

        pass

    def area(self):
        """Defines a function for area of a geometry
        This function is not defined and can't be used

        It raises an error message to the developer to
        define it before use
        """

        raise Exception("area() is not implemented")
