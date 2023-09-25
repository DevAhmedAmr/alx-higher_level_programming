#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0

    if my_list is None:
        return 0
    try:
        for counter in range(x):

            print(my_list[counter], end="")

            if counter == x-1:
                print("")
            counter = counter+1

    except Exception:
        print("", end="")

    return counter
