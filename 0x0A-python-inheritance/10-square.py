#!/usr/bin/python3
"""old _ empty class  """
Rectangle  = __import__("9-rectangle").Rectangle 


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        """__init__"""
        super().__init__(size, size)        
        self.integer_validator("size", size)
        self.__size=size
        
    def area(self):
        """area"""
        return self.__size * 2
