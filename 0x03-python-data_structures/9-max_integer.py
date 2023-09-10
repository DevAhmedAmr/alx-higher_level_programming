#!/usr/bin/python3
def max_integer(my_list=[]):

    max_integer = 0
    my_list_len = len(my_list)

    if my_list_len == 0:
        return None

    for i in range(my_list_len):

        if my_list[i] > max_integer:
            max_integer = my_list[i]

    return max_integer
