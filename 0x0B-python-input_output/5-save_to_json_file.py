#!/usr/bin/python3
"""json module"""
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file,
    using a JSON representation:

    Args:
            my_obj (_type_): string to be saved into a file
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
