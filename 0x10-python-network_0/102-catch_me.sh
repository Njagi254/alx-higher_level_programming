#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me
curl -X GET -H "origin: HolbertonSchool" 0.0.0.0:5000/catch_me -s | grep -o 'You got me!'
