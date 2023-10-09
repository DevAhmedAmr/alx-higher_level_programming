#!/usr/bin/python3
"""is_kind_of_class """


def inherits_from(obj, a_class):
    """is_kind_of_class """
    return False if type(obj) is a_class else isinstance(obj, a_class)
