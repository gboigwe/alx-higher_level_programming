#!/usr/bin/python3
"""Converts a Python object into a JSON string."""


import json


def to_json_string(my_obj):
    """Converts a Python object into a JSON string.

    Args:
        my_obj: The Python object to be converted.
        Must be JSON-serializable.

    Returns:
        str: The JSON string representation of
        the provided object.
    """

    return json.dumps(my_obj)
