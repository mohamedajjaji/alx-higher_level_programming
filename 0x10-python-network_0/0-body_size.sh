#!/bin/bash
# Use curl to send a request to the URL, store the response body size in bytes
curl -sI "$1" | awk '/Content-Length/{print $2}'
