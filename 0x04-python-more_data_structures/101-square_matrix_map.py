#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda element : list(map(lambda i: i*i,element)),matrix))



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)