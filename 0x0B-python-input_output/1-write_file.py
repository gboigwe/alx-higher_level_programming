#!/usr/bin/python3
"""Defining a function that writes file"""


def write_file(filename="", text=""):
    """This function writes the file

    Args:
        filename: writes a file into filename

    Returns:
        The number of characters inside
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
