#!/usr/bin/env bash
# This script sends a request to a given URL and displays the size of the response body in bytes

url="$1"
response=$(curl -s "$url")
size=${#response}

echo "$size"
