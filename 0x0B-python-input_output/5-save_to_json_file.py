#!/usr/bin/python3
"""Define a function that saves a JSON file
as string"""


import json


def save_to_json_file(my_obj, filename):
    """Overwrite a file with python objects
    using JSON
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
