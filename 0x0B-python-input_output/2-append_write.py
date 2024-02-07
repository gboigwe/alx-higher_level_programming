#!/usr/bin/python3
"""Defining a function that appends to a file"""


def append_write(filename="", text=""):
    """This function writes the file

    Args:
        filename: writes a file into filename

    Returns:
        The number of characters inside
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
