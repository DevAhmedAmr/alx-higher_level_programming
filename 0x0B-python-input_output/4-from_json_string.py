#!/usr/bin/python3
"""json module"""
import json


def from_json_string(my_str):
    """function that returns an object (Python data structure) 
    represented by a JSON string:

    Args:
            my_obj (_type_): string to be con converted
    """
    return json.loads(my_str)
