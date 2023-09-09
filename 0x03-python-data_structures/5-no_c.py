#!/usr/bin/python3
def no_c(my_string):
    strCpy = ""

    if not my_string:
        return strCpy

    for i in range(len(my_string)):
        if ("Cc" not in my_string):
            strCpy += my_string[i]

    return (strCpy)
