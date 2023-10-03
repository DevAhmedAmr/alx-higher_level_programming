#!/usr/bin/python3
"""_summary_"""


def matrix_divided(matrix, div):
    matrix_divided_arr = []
    length = set()
    row_size = 0
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, (list)):
        raise TypeError(error_msg)

    for i in matrix:
        tmp = []

        if not isinstance(i, (list)):
            raise TypeError(error_msg)

        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(error_msg)
            tmp.append(round(j/div, 2))
            row_size += 1

        length.add(row_size)
        row_size = 0
        matrix_divided_arr.append(tmp)

    if len(length) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    return matrix_divided_arr
