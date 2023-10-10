#!/usr/bin/python3

""" class_to_jso n"""
def class_to_json(obj):
    """ class_to_json

    Args:
            obj (_type_): _description_

    Returns:
            _type_: _description_
    """
    my_dictionary = dict()
    my_dictionary["name"] = obj.name
    my_dictionary["number"] = obj.number
    return obj.__dict__
