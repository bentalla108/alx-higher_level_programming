#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_ = [[matrix[j][i]**2 for i in range(len(matrix[j]))] for j in range(len(matrix))]
    return matrix_
