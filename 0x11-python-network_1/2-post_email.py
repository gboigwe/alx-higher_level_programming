#!/usr/bin/python3
"""Write a Python script that takes in a URL
and an email, sends a POST request to the
passed URL with the email as a parameter,
and displays the body of the response
(decoded in utf-8)
"""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    dict_email = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(dict_email)
    data = email.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as res:
        html = res.read()
        print(html.decode('utf-8'))
