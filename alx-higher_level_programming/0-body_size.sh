#!/bin/bash
# Script that takes a URL, sends a GET request to it, and displays the size of the response body
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
