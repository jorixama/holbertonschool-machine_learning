#!/usr/bin/env python3
import numpy as np
"""a function that concates two matrices"""

def np_cat(mat1, mat2, axis = 0):
    """returns concatenated matrix"""
    return np.concatenate((mat1, mat2), axis)
def np_cat(mat1, mat2, axis = 1):
    return np.concatenate((mat1, mat2), axis=1)
def np_cat(mat1, mat3, axis = 1):
    return np.concatenate((mat1, mat3), axis=1)
return result
mat1 = np.array([[11, 22, 33], [44, 55, 66]])
mat2 = np.array([[1, 2, 3], [4, 5, 6]])
mat3 = np.array([[7], [8]])
