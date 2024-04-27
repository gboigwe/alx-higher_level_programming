#!/usr/bin/python3
"""
    A Python script that takes in a letter
    sends a POST request to
    http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        data = r.json()
        if data:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
