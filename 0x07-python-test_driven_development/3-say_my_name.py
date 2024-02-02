#!/usr/bin/python3
"""
Defines a function that says your name.
"""


def say_my_name(first_name, last_name=""):
    """
    Say your name.
    Reply first_name and last_name in strings otherwise, TypeError
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
