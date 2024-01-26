#!/usr/bin/python3
"urllib.request"
import urllib.request

if __name__ == "__main__":
    "script that fetches https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")
