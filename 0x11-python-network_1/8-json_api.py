#!/usr/bin/python3
""" urlLib"""
import requests
import sys

if __name__ == "__main__":
    """Python script that takes in a URL, sends a request to
    the URL and displays the body of the response."""
    url = url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    values = {"q": q}
    r = requests.post(url, values)
    try:
        if r.json().get("id") is None or r.json().get("name") is None:
            print("No result")
        else:
            print("[{}] {}".format(r.json()["id"], r.json()["name"]))
    except ValueError:
        print("Not a valid JSON")
