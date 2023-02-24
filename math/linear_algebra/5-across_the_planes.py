#!/usr/bin/env python3
def add_matrices2D(mat1, mat2):
    mat = []
    if len(mat1) != len(mat2[0]) or len(mat1) != len(mat2):
        return None
    for i in range(len(mat1)):
        row =[]
        for j in range(len(mat1[0])):
            row.append((mat1[i][j]) + (mat2[i][j]))
        mat.append(row)
    return mat
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(add_matrices2D(mat1, mat2))
print(mat1)
print(mat2)
print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))
