#!/usr/bin/env python3
"""a function that adds two matrices element-wise"""


def add_matrices2D(mat1, mat2):
    """adds two matrices element-wise"""
    mat = []
    if len(mat1) != len(mat2[0]) or len(mat1) != len(mat2):
        return None
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1 + mat2)
        mat.append(row)
    return mat
