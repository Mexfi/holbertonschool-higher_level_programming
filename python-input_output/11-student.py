#!/usr/bin/python3
def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle"""
    if n <= 0:
        return []

    triangle = [[1]]  # first row

    for i in range(1, n):
        prev = triangle[-1]
        row = [1]  # first element

        # middle values
        for j in range(1, i):
            row.append(prev[j-1] + prev[j])

        row.append(1)  # last element
        triangle.append(row)

    return triangle
