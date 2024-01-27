#!/usr/bin/python3
""" urlLib"""
import requests
import sys

if __name__ == "__main__":
    "Python script that fetches https://alx-intranet.hbtn.io/status"
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers)
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
