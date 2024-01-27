#!/usr/bin/python3
import urllib.request
import urllib.error
import sys

""" urlLib"""

if __name__ == "__main__":
    """python script that takes in a URL,
            sends a request to the URL and displays the
    body of the response (decoded in utf-8)."""

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print(e.reason)
