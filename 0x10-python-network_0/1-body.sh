#!/bin/bash
# Bash script that takes URL, sends a GET request to URL, and displays the body response
curl -sX GET "$1" -L 200
