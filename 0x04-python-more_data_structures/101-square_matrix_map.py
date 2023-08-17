#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    matrix_m = list(map(lambda x: list(map(lambda y: y**2, x)), matrix))
    return (matrix_m)
