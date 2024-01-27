#!/usr/bin/python3
"urllib.request"
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    """Python script that takes in a URL and an email, sends a
    POST request to the passed URL with the email as a parameter, and
    displays the body of the response (decoded in utf-8)"""

    link = sys.argv[1]
    Email = sys.argv[2]

    values = {"email": Email}
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")

    req = urllib.request.Request(link, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
