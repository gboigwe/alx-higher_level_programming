#!/usr/bin/python3
"""
Converts a Python object into a JSON string.

This function takes a Python object (`my_obj`) as input and serializes it into a JSON
string representation. It utilizes the `json.dumps` function for the conversion.

Args:
    my_obj (dict, list, tuple, str, int, float, bool, or custom object): The
        Python object to be converted.

Returns:
    str: The JSON string representation of the provided object.
"""


import json


def to_json_string(my_obj):
    """Converts a Python object into a JSON string.

    This function implements PEP 257 conventions for docstrings, providing a clear
    summary, detailed parameter explanations, return value descriptions, and potential
    errors.

    Args:
        my_obj (dict, list, tuple, str, int, float, bool, or custom object): The
            Python object to be converted. Must be JSON-serializable.

    Returns:
        str: The JSON string representation of the provided object.
    """

    return json.dumps(my_obj)
