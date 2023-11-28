#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy.


"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy
    """
    if not m_a or not all(row for row in m_a) or not m_b or not all(
            row for row in m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    try:
        result = np.dot(np.array(m_a), np.array(m_b))
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e

    return result
