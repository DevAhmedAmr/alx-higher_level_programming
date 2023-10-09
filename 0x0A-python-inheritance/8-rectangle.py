#!/usr/bin/python3
"""empty class  """
BaseGeometry=__import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """empty class  """
    def __init__(self, width, height):
        
        self.integer_validator(width,height)
        self.__width=width
        self.__height=height
