#!/usr/bin/python3
"""function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """_summary_

    Args:
            filename (str, optional): _description_. Defaults to "".
            text (str, optional): _description_. Defaults to "".

    Returns:
            _type_: _description_
    """
    with open(filename, "a") as file:
        return file.write(text)
