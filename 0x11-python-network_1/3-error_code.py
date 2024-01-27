#!/usr/bin/python3
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
            print(response.read())
    except urllib.error.URLError as e:
        print(e.reason)
