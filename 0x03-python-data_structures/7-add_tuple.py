#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):


    return None


def tuple_to_list(tuple_a=()):

    tuple_a_len = len(tuple_a)
    list_a = []

    for i in range(tuple_a_len):
        if tuple_a_len == 1:
            list_a.append(tuple_a[i])
            list_a.append(0)

        elif tuple_a_len == 2:
            list_a.append(tuple_a[i])

    if tuple_a_len == 0:
        list_a.append(0)
        list_a.append(0)

    return list_a
