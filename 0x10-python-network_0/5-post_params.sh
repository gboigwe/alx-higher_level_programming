#!/bin/bash
# Script that takes URL, sends POST request to passed URL, and display body of response
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
