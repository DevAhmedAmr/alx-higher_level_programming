#!/usr/bin/python3
""" Python script that takes 2 arguments in order to solve this challenge.
"""
import sys
import requests

"""requests lib used for post requests and getting responds"""

if "__main__" == __name__:
    """test"""
    repo_name = sys.argv[1]
    username = sys.argv[2]

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
                    f"{r.json()[i]['sha']}: "
                    f"{r.json()[i]['commit']['author']['name']}"
                )

        except:
            pass
        else:
            pass
