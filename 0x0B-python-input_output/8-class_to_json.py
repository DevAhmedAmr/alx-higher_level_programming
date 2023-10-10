#!/usr/bin/python3
"""json module"""
import json


def class_to_json(obj):
    """_summary_

    Args:
            obj (_type_): _description_

    Returns:
            _type_: _description_
    """
    my_dictionary = dict()
    my_dictionary["name"] = obj.name
    my_dictionary["number"] = obj.number
    return json.dumps(my_dictionary)
