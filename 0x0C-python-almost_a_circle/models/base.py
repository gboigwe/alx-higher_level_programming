#!/usr/bin/python3
"""Created a Base class

Base class has a private class attribute

This class is the base class for other attributesls
"""
import json
import csv


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Saving JSON string in list_objs to a file
        Args:
            cls (cls): class
            list_objs (file): list instances inheriting from Base
        """
        file_name = "{:s}.json".format(cls.__name__)
        input = []

        if list_objs is not None:
            for obj in range(len(list_objs)):
                input.append(cls.to_dictionary(list_objs[obj]))

        with open(file_name, mode="w", encoding="utf-8") as a_file:
            a_file.write(cls.to_json_string(input))
