#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -s -L  -X PUT  -H 'Origin: School' localhost:5000/catch_me_3
