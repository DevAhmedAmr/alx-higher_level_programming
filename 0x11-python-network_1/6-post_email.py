#!/usr/bin/python3
""" urlLib"""
import requests
import sys

if __name__ == "__main__":
    """Python script that takes in a URL and an email address, sends a
    POST request to the passed URL with the email as a parameter, and finally
        displays the body of the response."""
    url = sys.argv[1]
    email = sys.argv[2]
    value = {"email": email}
    r = requests.post(url, data=value)
    print(r.text)
