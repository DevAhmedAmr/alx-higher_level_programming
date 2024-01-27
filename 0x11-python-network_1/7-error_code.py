#!/usr/bin/python3
""" urlLib"""
import requests
import sys

if __name__ == "__main__":
    """Python script that takes in a URL, sends a request to
    the URL and displays the body of the response."""
    url = sys.argv[1]
    r = requests.post(url)

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
