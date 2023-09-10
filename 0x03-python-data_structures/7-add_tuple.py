#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return None
    
    list_a = tuple_to_list(tuple_a)
    list_b = tuple_to_list(tuple_b)

    sum_num1 = list_a[0]+list_b[0]
    sum_num2 = list_a[1]+list_b[1]

    return (sum_num1, sum_num2)


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
