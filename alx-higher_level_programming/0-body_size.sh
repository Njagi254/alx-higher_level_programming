#!/bin/bash
# Script that takes a URL, sends a GET request to it, and displays the size of the response body
curl -s "$1" | wc -c
