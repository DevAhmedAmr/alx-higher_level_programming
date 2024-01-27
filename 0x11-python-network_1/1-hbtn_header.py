#!/usr/bin/python3
"urllib.request"
import urllib.request
import sys

if __name__ == "__main__":
    "script that fetches X-Request-Id var from the header of the response"
    link = sys.argv[1]
    Email = sys.argv[2]

    with urllib.request.urlopen(link) as response:
        header_info = response.info()
        print(header_info["X-Request-Id"])
