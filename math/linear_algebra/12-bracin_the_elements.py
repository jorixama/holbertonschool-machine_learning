#!/usr/bin/env python3
"""bracing"""

import numpy as np
"""transpose numpy"""
mat1 = np.array([[11, 22, 33], [44, 55, 66]])
mat2 = np.array([[1, 2, 3], [4, 5, 6]])

mat1 = mat1.T
mat2 = mat2.T
print(mat1)
print(mat2)

print("Add:")
print(np.add(mat1, mat2))
print("Subtract:")
print(np.subtract(mat1, mat2))
print("Multiply:")
print(np.multiply(mat1, mat2))
print("Divide:")
print(np.divide(mat1, mat2))
