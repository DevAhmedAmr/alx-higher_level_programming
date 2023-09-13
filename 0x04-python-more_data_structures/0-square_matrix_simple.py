#!/usr/bin/python3
def square_matrix_simple2(matrix=[]):
    matrix_sq = []

    if matrix is None:
        return None

    for i in range(len(matrix)):

        sub_matrix_sq = []

        if matrix[i] is None:
            matrix_sq.append(None)
            continue

        for j in range(len(matrix[i])):
            sub_matrix_sq.append(matrix[i][j]*matrix[i][j])
        matrix_sq.append(sub_matrix_sq)

    return matrix_sq


def square_matrix_simple(matrix=[]):
    matrix_sq = []
    x = matrix[0]
    for i in matrix:
        result = map((lambda x: x*x), i)
        matrix_sq.append(list(result))
    return matrix_sq
