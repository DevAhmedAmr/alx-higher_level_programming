#!/usr/bin/python3
"""Sends a search request for a given string to the Star Wars API.

Usage: ./9-starwars.py <search string>
  - The search request is sent to the Star Wars API search people endpoint.
"""
import sys
import requests

"requests lib"
if "__main__" == __name__:
    username = sys.argv[1]
    repo_name = sys.argv[2]

    r = requests.get(
        url=f"https://api.github.com/repos/{username}/{repo_name}/commits",
        data={"owner": username, "repo": repo_name},
        headers={
            "Accept": "application/vnd.github.v3+json",
        },
    )
    if r.status_code >= 200 and r.status_code <= 300:
        try:
            for i in range(10):
                print(
                    f"{r.json()[i]['sha']}: {r.json()[i]['commit']['author']['name']}"
                )
        except:
            pass
        else:
            pass
