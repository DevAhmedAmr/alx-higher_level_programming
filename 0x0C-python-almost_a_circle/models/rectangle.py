#!/usr/bin/python3
""" Module class base
"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y setter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y getter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a Rectangle instance."""
        return self.width*self.height

    def display(self):
        """display"""
        
        for i in range(self.y):
            print("")
        for i in range(self.height):
            print(self.x * " ", end="")
            print("#"*self.width)

    def __str__(self):
        """ override for __str__ method"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update"""
        if len(args) > 0:
            self.id = args[0]
            if len(args) <= 1:
                return

            self.width = args[1]
            if len(args) <= 2:
                return

            self.height = args[2]
            if len(args) <= 3:
                return
            self.x = args[3]
            if len(args) <= 4:
                return
            self.y = args[4]
        if len(kwargs) > 0:
            if kwargs.get("id") is not None:
                self.id = kwargs["id"]

            if kwargs.get("width") is not None:
                self.width = kwargs["width"]

            if kwargs.get("height") is not None:
                self.height = kwargs["height"]

            if kwargs.get("x") is not None:
                self.x = kwargs["x"]

            if kwargs.get("y") is not None:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """to_dictionary"""
        return {'id': self.id,  'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y,}
