#!/usr/bin/python3
Rectangle = __import__("rectangle").Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ override for __str__ method"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """sqaure"""
        return self.width

    @size.setter
    def size(self, size):
        """setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update"""
        elements = (self.id, self.size, self.x, self.y)
        if len(args) > 0:
            self.id, self.size, self.x, self.y = args + \
                elements[len(args):len(elements)]
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {"id": self.id, "x": self.x, 
                "size": self.size, "y": self.y}