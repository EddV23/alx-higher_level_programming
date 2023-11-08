#!/usr/bin/python3
"""computes the square value of all integers of a matrix"""


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            new_row += [x ** 2]
        new_matrix += [new_row]
    return new_matrix
    """
    new_matrix = []
    for row in matrix:
        new_row = [x ** 2 for x in row]
        new_matrix += [new_row]
    return new_matrix

    new_matrix = []
    for row in matrix:
        new_row = [x**2 for x in row]
        new_matrix.append(new_row)
    return new_matrix

    new_matrix = [[x**2 for x in row] for row in matrix]
    return new_matrix

    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            new_row.append(x ** 2)
        new_matrix.append(new_row)
    return new_matrix

    new_matrix = []
    for row in matrix:
        result = list(map(lambda x: x * x, row))
        new_matrix.append(result)
    return new_matrix

    #return [[num ** 2 for num in row] for row in matrix]
    """
