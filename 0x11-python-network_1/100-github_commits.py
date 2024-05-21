#!/usr/bin/python3
"""
    Python script that takes 2 arguments
    in order to solve this challenge
"""

import sys
import requests


if __name__ == "__main__":
    url_api = "https://api.github.com/repos/{}/{}/commits"
    .format(sys.argv[2],
            sys.argv[1])
    r = requests.get(url_api)
    d = r.json()
    for i in range(10):
        print("{}: {}"
                .format(
                    d[i]["sha"], d[i]["commit"]["author"]["name"]
                    ))
