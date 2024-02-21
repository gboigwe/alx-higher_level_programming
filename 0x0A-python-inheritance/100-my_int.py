#!/usr/bin/python3
"""Creating a class that acts like int
    Acts like but in an inverted way
"""


class MyInt(int):
    """Created the class"""

    def __init__(self, value):
        """Initializing the class
        Args:
            value : value is validated
        """

        self.__value = value
        super().__init__()

    def __eq__(self, other):
        """Defining a function that handles == operator
        Args:
            other : Other is inverted
        Returns:
            Returning the inverted value handled by eq function
        """

        return not super().__eq__(other)

    def __ne__(self, other):
        """Defining a function that handles != operator
        Args:
            other : Other is inverted
        Returns:
            Returning the inverted value handled by ne function
        """

        return not super().__ne__(other)
