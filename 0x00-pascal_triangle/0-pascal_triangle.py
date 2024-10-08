#!/usr/bin/python3
"""file ya Pascal's Triangle"""


def pascal_triangle(n):
    """method itanga list of lists of integers Pascal’s triangle of n"""
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
