#!/usr/bin/python3
"""Write a function that creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """Delivering the python object package"""
    with open(filename, "w") as f:
        return json.load(f)