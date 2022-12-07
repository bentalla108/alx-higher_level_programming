#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_ = []
    for i in matrix:
        matrix_.append(list(map((lambda x: x ** 2), i)))
    return matrix_
