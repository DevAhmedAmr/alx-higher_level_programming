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
        print("\n", end="")

    return counter

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 992)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
