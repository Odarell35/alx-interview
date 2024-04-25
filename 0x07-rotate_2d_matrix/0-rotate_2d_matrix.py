#!/usr/bin/python3
"""0. Rotate 2D Matrix"""

def rotate_2d_matrix(matrix):
    """
    rotate_2d_matrix(matrix)
    print(matrix)
    """
    length = len(matrix)
    for i in range(length):
        for j in range(i, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(length):
        matrix[i] = matrix[i][::-1]

