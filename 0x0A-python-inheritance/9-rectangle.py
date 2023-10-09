#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""empty class  """


class Rectangle(BaseGeometry):
    """empty class  """

    def __init__(self, width, height):
        """__init__   """

        self.integer_validator("height", height)
        self.integer_validator("width", width)

        self.__width = width
        self.__height = height
        
    def area(self):
        """area"""
        return self.__width * self.__height
    
    def __str__(self):
        """__str__"""
        return "[Rectangle] {}/{}".format(self.__width,self.__height)
        
    

r = Rectangle(3, 5)

print(r)
print(r.area())
