#!/usr/bin/python3


def pascal_triangle(n):
    if n <= 0:
        return []

    angle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = angle[i - 1][j - 1] + angle[i - 1][j]
        angle.append(row)

    return angle
