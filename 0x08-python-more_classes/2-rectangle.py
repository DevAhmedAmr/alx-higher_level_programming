#!/usr/bin/python3

"""_summary_"""


class Rectangle:
    """ Rectangle """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        
    def area(self):
        return self.__height*self.__width
    
    def perimeter(self):
        return (self.__height+self.__width)*2

    if __name__=="__main__":
        Rectangle = __import__('2-rectangle').Rectangle
        my_rectangle = Rectangle(2, 4)
        print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
        print("--")
        my_rectangle.width = 10
        my_rectangle.height = 3
        print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))