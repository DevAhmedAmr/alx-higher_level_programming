#!/usr/bin/python3
"""summary"""


def text_indentation(text):
    """text_indentation"""
    flag = 1

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):

        if flag == 1 and text[i] == " ":
            continue
        else:
            flag = 0

        print(text[i], end="")

        if text[i] == "." or text[i] == "?" or text[i] == ":":

            if i < len(text) - 1 and text[i+1] == " ":
                flag = 1

            print("\n")
