#!/bin/bash
# Bash script that takes URL, sends a GET request to URL, and displays the body response
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
