#!/usr/bin/python3
"""Defining a function that reads file"""


def read_file(filename=""):
    """This function reads the file

    Args:
        filename: Takes in any file the user pass in

    Then the file gets read by f.read()
    """

    with open(filename, mode="r", encoding="utf-8") as f:
        return f.read()