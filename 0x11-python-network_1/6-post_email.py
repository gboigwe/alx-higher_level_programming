#!/usr/bin/python3
"""
"""
import sys
import requests


if __name__ == "__main__":
    post_email = {'email': sys.argv[2]}
    email = requests.post(sys.argv[1], post_email)
    print(email.text)
