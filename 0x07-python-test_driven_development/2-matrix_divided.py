#!/usr/bin/python3
"""
Module for dividing all elements of a matrix.


"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        str = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(str)
    """
    if ((type(matrix) is not list) or (matrix == []) or
        (not all(isinstance(row, list) for row in matrix)) or
        (not all(isinstance(i, int) or (type(i) is float)
                 for i in [n for row in matrix for n in row]))):
        str = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(str)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        str = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(str)

    for row in matrix:
        str = "matrix must be a matrix (list of lists) of integers/floats"
        if type(row) is not list or len(row) == 0:
            raise TypeError(str)
        for col in matrix[0]:
            if type(col) is not int and type(col) is not float:
                raise TypeError(str)

    mat = [row[:] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            mat[row][col] = round(matrix[row][col] / div, 2)
    return mat

    return [[round(elem / div, 2) for elem in row] for row in matrix]
    """
