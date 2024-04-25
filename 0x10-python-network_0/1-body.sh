#!/bin/bash
# Bash script that takes URL, sends a GET request to URL, and displays the body response
curl -s -X GET "$1" -o /dev/null -w "%{http_code}" | grep -q 200 && curl -s "$1"
