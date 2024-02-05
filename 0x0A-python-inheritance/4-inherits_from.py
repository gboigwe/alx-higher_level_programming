#!/usr/bin/python3
"""Defines a function that checks the object is if
the instance of a class that inherited directly
or indirectly from the specified class is True
"""


def inherits_from(obj, a_class):
    """This function checks inheritance of the subclass of object

    Args:
        obj: The object to be considered

        a_class: instance considered

    Return True if isinstance of subclass is True otherwise false
    """

    if issubclass(type(obj), a_class):
        return True
    return False
