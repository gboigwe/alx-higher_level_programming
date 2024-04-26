#!/usr/bin/python3
"""
    Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        res = """
Body response:$
    - type: {}$
    - content: {}$
    - utf8 content: {}$
    """.format(type(html), html, html.decode('utf-8'))
        print(res)
