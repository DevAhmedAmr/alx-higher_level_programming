#!/usr/bin/python3
""" urlLib"""
import requests


if __name__ == "__main__":
    "Python script that fetches https://alx-intranet.hbtn.io/status"

    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
