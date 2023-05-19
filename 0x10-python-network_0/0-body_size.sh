#!/bin/bash

read -p "Enter URL:" URL
BODY=$(curl -s -w "%{size_download}" -o /dev/null "&URL")
echo "Size of body: $BODY bytes"
