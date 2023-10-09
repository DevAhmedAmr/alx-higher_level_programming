#!/usr/bin/python3
"""empty class  """
BaseGeometry=__import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """empty class  """
    def __init__(self, width, height):
        
        self.integer_validator("height",height)
        self.integer_validator("width",width)

        self.__width=width
        self.__height=height
r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
