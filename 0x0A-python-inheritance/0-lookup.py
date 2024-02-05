#!/usr/bin/python3
""""Defines a function that returns a list"""


def lookup(obj):
    """Function lookup defined
    obj1: created to access the dir of object obj
    Returns the dir of object obj
    """

    obj1 = dir(obj)
    return obj1
