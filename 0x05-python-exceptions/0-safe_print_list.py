#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0

    if my_list is None:
        return 0
    try:
        for i in range(x):

            print(my_list[i], end="")

            if i == x-1:
                print("")
            i = i+1

    except Exception:
        print("", end="")

    return i
