#!/usr/bin/python3
"""Created a class Square, that inherits from rectangle"""


Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """Defining a Square class
    Initializing and inheriting Rectangle class

    Args:
        size: calculate for size
    """

    def __init__(self, size):
        """Initializaion is called on the class
            size is initialized
        """

        if self.integer_validator("size", size):
            self.__size = size
        super().__init__(self, size)

    def area(self):
        """Defines an area for the square"""

        return super().area()
