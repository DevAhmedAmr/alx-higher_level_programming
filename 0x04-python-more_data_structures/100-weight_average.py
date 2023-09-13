#!/usr/bin/python3
def weight_average(my_list=[]):
    list_len = len(my_list)
    total_avg = 0
    weight_avg = 0

    if list_len == 0:
        return 0

    for i in range(list_len):
        multi = 1

        for j in range(len(my_list[i])):
            multi *= my_list[i][j]

        total_avg += multi
        weight_avg += my_list[i][1]

    return total_avg/weight_avg
