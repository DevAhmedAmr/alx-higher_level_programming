#!/usr/bin/python3

"""_summary_"""


class Rectangle:
    """ Rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width """
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height*self.__width

    def perimeter(self):

        if (self.height == 0 or self.width == 0):
            return 0

        return (self.__height+self.__width)*2

    def __str__(self):
        string = ""

        if self.width == 0 or self.height == 0:
            return string

        for i in range(self.height):
            string += (str(self.print_symbol) * self.width)

            if i != self.height-1:
                string += "\n"
        return string

    def __repr__(self):
        return f"Rectangle({self.width:d}, {self.height})"

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
        
    @classmethod 
    def square(cls, size=0):
        return(cls(size,size))
    
my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
