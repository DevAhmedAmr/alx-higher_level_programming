#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def my_print(self):
        for i in range(self.size):
            for j in range(self.size):
                print("#",end="")
            print("")
        if self.size == 0 :
            print("")