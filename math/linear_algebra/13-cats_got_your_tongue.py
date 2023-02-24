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
