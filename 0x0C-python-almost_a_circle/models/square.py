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
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
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


# if __name__ == "__main__":

#     r1 = Rectangle(10, 7, 2, 8)
#     r2 = Rectangle(2, 4)
#     list_rectangles_input = [r1, r2]

#     Rectangle.save_to_file(list_rectangles_input)

#     list_rectangles_output = Rectangle.load_from_file()

#     for rect in list_rectangles_input:
#         print("[{}] {}".format(id(rect), rect))

#     print("---")

#     for rect in list_rectangles_output:
#         print("[{}] {}".format(id(rect), rect))

#     print("---")
#     print("---")

#     s1 = Square(5)
#     s2 = Square(7, 9, 1)
#     list_squares_input = [s1, s2]

#     Square.save_to_file(list_squares_input)

#     list_squares_output = Square.load_from_file()

#     for square in list_squares_input:
#         print("[{}] {}".format(id(square), square))

#     print("---")

#     for square in list_squares_output:
#         print("[{}] {}".format(id(square), square))