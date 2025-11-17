#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Args:
        matrix: A list of lists representing the matrix.
                Each inner list contains integers.
    """
    for row in matrix:
        for i, num in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(num), end="")
            else:
                print("{:d}".format(num), end=" ")
        print()
