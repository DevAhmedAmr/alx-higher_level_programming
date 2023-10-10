#!/usr/bin/python3
"""json module"""
import json


def load_from_json_file(filename):
    """  function that creates an Object from a “JSON file”

    Args:
            filename (file): to be printed
    """
    with open(filename, "r") as file:
        return json.load(file)
