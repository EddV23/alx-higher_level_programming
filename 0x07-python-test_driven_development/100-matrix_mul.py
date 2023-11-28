#!/usr/bin/python3
"""
Module for matrix multiplication.


"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(
            row, list) for row in m_b):
        str2 = "m_a must be a list of lists or m_b must be a list of lists"
        raise TypeError(str2)

    if not m_a or not all(row for row in m_a) or not m_b or not all(
            row for row in m_b):
        str3 = "m_a can't be empty or m_b can't be empty"
        raise ValueError(str3)

    if not all(isinstance(element, (int, float)) for row in m_a for element in
               row) or not all(isinstance(element, (int, float)) for row in m_b
                               for element in row):
        str4_a = "m_a should contain only integers or floats or "
        str4_b = "m_b should contain only integers or floats"
        raise TypeError(str4_a + str4_b)

    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(
            len(row) == len(m_b[0]) for row in m_b):
        str5_a = "each row of m_a must be of the same size or "
        str5_b = "each row of m_b must be of the same size"
        raise TypeError(str5_a + str5_b)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)]
              for row_a in m_a]

    return result
