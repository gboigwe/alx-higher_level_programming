#!/bin/bash
# A script that takes a URL, sends request and get response.
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
