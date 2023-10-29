#!/usr/bin/python3
"""
This module has has a matrix divided function
"""


def matrix_divided(matrix, div):
    """
    to return a new matrix all values divided by a div
    Args:
        @matrix : lis of numbers(ints and floats).
        @div: the divider number,must be >= 0.
    """
    type_e_msg = 'matrix must be a matrix (list of lists) of integers/floats'
    length_e_msg = 'Each row of the matrix must have the same size'
    type_div_e_msg = 'div must be a number'
    zero_div_e_msg = 'division by zero'

    length = 0
    if type(matrix) is not list:
        raise TypeError(type_e_msg)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(type_e_msg)
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(type_e_msg)
        if len(row) is not length and length is not 0:
            raise TypeError(length_e_msg)
        length = len(row)

    if type(div) not in [int, float]:
        raise TypeError(type_div_e_msg)
    if div is 0:
        raise ZeroDivisionError(zero_div_e_msg)

    return [[round(nb / div, 2) for nb in row] for row in matrix]
