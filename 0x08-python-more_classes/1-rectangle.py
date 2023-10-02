#!/usr/bin/python3

"""_summary_"""


class Rectangle:
    """ Rectangle """
    
    def __init__(self, width=0,height=0):
        self.__width = width
        self.__height=height
        
		
    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self,value):
        """ width """
        if type(value)!= int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width=value

    @property
    def height(self):
        """ height """
        return self.__height
    
    @height.setter
    def height(self,value):
        """ height """
        if type(value)!= int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height=value
