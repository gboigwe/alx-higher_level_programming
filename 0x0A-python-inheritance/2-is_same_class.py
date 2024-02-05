#!/usr/bin/python3
"""Defines a function that checks for data type"""


def is_same_class(obj, a_class):
    """A function that checks the data type of object

    Args:
        obj: The object to be considered

        a_class: Datatype to be considered

    Return True if datatype match and false if it doesn't
    """

    if a_class is type(obj):
        return True
    else:
        return False
