#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squ_matrix = []
    idx = 0
    for i in matrix:
        sub_mat = []
        count = 0
        for j in matrix[idx]:
            sqr = matrix[idx][count] ** 2
            sub_mat.append(sqr)
            count = count + 1
        squ_matrix.append(sub_mat)
        idx = idx + 1
    return (squ_matrix)
