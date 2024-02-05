#!/usr/bin/python3
"""Defines a class that sorts a list"""


class MyList(list):
    """list is passed as an object
    list as an object in class MyList
    """

    def print_sorted(self):
        print(sorted(self))
