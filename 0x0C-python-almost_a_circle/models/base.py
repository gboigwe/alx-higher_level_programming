#!/usr/bin/python3
"""Created a Base class

Base class has a private class attribute

This class is the base class for other attributesls
"""


class Base:
    """
    __nb_objects - Variable name for class Base

    Args:
        id (int): Public instance attribute

    Assuming id is integer and is not None
    Assign an id

    Otherwise increment the class variable
    and assign the new value to a public instance attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing base class with an id

        incrementing each instance by 1
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string representation of list_dictionaries
        Args:
            list_dictionaries (obj): object
        Returns:
            JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
