#!/usr/bin/env python3
def matrix_shape(matrix):
    result=[]
    result.append(len(matrix))
    for i in range(len(matrix)-1):
        result.append(len(matrix))
        if isinstance(matrix[i][i],list):
            result.append(len(matrix[i][i]))
    return result
