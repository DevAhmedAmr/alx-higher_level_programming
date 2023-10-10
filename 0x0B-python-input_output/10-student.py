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
        dictionary = {}
        if attrs is None:
            return vars(self)
        for i in attrs:
            if i in vars(self).keys():
                dictionary[i]=vars(self)[i]
            
        return dictionary

student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)