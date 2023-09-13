#!/usr/bin/python3
def best_score(a_dictionary):
    biggest_integer_value = -999999999999999
    biggest_integer_key = None

    if a_dictionary is None:
        return None

    for i in a_dictionary:
        if a_dictionary[i] > biggest_integer_value:
            biggest_integer_value = a_dictionary[i]
            biggest_integer_key = i

    return biggest_integer_key
