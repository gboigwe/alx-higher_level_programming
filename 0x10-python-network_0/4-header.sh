#!/bin/bash
# Bash script that takes a URL as an arg, sends a GET request to URL, and displays body of response
curl -s -X GET -H "X-School-User-Id:98" "$1" || echo "Error"
