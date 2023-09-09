#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return 
    strCpy=""
    for i in range(len(my_string)):
        if (my_string[i]!="C" and my_string[i]!="c"):
            strCpy += my_string[i]
    return (strCpy)



