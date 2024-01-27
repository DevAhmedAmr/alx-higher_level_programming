#!/usr/bin/python3
""" urlLib"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    """python script that takes in a URL,
            sends a request to the URL and displays the
    body of the response (decoded in utf-8)."""
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
