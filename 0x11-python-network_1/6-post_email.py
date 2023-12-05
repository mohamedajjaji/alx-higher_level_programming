#!/usr/bin/python3
""" Ssends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    req = requests.post(url, data=value)
    print(req.text)
