#!/usr/bin/python3
"""json module"""
import os
import json
"""os module"""

"""Base"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string function"""
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file"""
        file_name = cls.__name__+".json"
        lst = []
        
        if list_objs:
            for element in list_objs:
                lst.append(element.to_dictionary())

        json_encoded = cls.to_json_string(lst)

        with open(file_name, "w") as file:
            file.write(json_encoded)

    def from_json_string(json_string):
        """from_json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(10, 10)
        else:
            new_instance = cls(10)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """load_from_file"""
        file_name = cls.__name__+".json"

        if os.path.exists(file_name) is False:
            return []

        with open(file_name, "r") as file:
            list_of_instance = cls.from_json_string(file.read())
            ls = []
            for instance in list_of_instance:
                x = cls.create(**instance)
                ls.append(x)
            return ls
