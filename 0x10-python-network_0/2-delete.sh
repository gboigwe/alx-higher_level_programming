#!/bin/bash
# Script sends DELETE request to first argument URL and displays response body
curl -sX DELETE "$1" -L 200
