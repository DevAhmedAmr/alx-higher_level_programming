#!/usr/bin/python3
"urllib.request"
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    "script that fetches X-Request-Id var from the header of the response"
    link = sys.argv[1]
    Email = sys.argv[2]

    values = {"email": Email}
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")

    req = urllib.request.Request(link, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
