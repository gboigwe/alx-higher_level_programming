#!/bin/bash
# A script that takes a URL, sends request and get response.
res_url=$(curl -s "$1")
content_length=${#res_url}
echo "$content_length"
