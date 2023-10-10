#!/usr/bin/python3
""" function that writes a string to a text file"""


def write_file(filename="", text=""):
    """write_file
            Args:
            filename (str, optional): the file name to be opened. Defaults to "".
            text (str, optional): text to be written to. Defaults to "". """
    with open(filename, "w+") as file:
        return file.write(text)

