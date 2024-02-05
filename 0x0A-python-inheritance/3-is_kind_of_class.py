#!/usr/bin/python3
"""Defines a function that checks
for instance of data
"""


def is_kind_of_class(obj, a_class):
    """This function checks the instance of the object

    Args:
        obj: The object to be considered

        a_class: Datatype to be considered

    Return True if isinstance is True otherwise false if it doesn't
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
