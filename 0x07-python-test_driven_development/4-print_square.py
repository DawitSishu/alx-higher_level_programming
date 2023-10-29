#!/usr/bin/python3
"""
this module supplies only print square function
"""


def print_square(size):
    """
    prints a squarw with #
    Args:
        @size: the length of side of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print(("#" * size + '\n') * size, end='')
