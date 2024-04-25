#!/usr/bin/env bash
# A script that takes a URL, sends request and get response.
url_arg="$1"
res_url=$(curl -s "url_arg")
content_length=${#res_url}

echo "$content_length"
