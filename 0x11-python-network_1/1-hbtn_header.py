#!/usr/bin/python3
""" Sends a request to the URL and displays the X-Request-Id
header variable of a request to a given URL.
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
