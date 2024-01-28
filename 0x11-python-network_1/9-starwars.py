#!/usr/bin/python3
"""Sends a search request for a given string to the Star Wars API.

Usage: ./9-starwars.py <search string>
  - The search request is sent to the Star Wars API search people endpoint.
"""
import sys
import requests

r = requests.post(
    url="https://api.github.com/octocat",
    data={
        "Authorization": "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",
        "X-GitHub-Api-Version": " 2022-11-28",
    },
)
print(r.text)
