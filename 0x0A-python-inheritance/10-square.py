#!/usr/bin/python3
"""old _ empty class  """
Rectangle  = __import__("9-rectangle").Rectangle 

class Square(Rectangle):
    def __init__(self, size):
        """__init__"""
        self.integer_validator("size", size)
        self.__size=size
        
    def area(self):
        """area"""
        return self.__size * self.__size
    
    def __str__(self):
        """__str__"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
