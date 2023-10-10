#!/usr/bin/python3
"""_summary_
Returns:
_type_: _description_"""


class Student:
    """_summary_
        """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """_summary_"""
        dictionary = {}
        if attrs is None:
            return vars(self)
        for i in attrs:
            if i in vars(self).keys():
                dictionary[i] = vars(self)[i]
                
    def reload_from_json(self, json):
        """_summary_

		Args:
			json (_type_): _description_
		"""
        if json.get("first_name"):
            self.first_name = json["first_name"]
            
        if json.get("last_name"):
            self.last_name= json["last_name"]
            
        if json.get("age"):
            self.age=json["age"]
        
