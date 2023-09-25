#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0

    if my_list is None:
        return 0
    try:
        for i in range(x):

            print(my_list[i], end="")

            if i == x-1:
                print("")
            counter = counter+1

    except Exception:
        print("", end="")

    return counter
