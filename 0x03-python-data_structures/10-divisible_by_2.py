#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None

    arr_len = len(my_list)
    is_divisible_by_2 = []

    for i in range(arr_len):
        if my_list[i] % 2 == 0:
            is_divisible_by_2.append(True)
        else:
            is_divisible_by_2.append(False)

    return is_divisible_by_2
