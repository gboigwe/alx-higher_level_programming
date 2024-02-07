#!/usr/bin/python3
"""Loads a JSON String from a python object."""


import json


def from_json_string(my_str):
    """Loads a JSON String from a python object.

    Args:
        my_str: The String to be considered.
        Must be a Python Object.

    Returns:
        objs: The loaded string.
    """

    return json.loads(my_str)
