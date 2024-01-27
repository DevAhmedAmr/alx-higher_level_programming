#!/usr/bin/python3
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read())
    except urllib.error.URLError as e:
        print(e.reason)
