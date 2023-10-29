#!/usr/bin/python3
""" This module has a add function to add numbers """


def add_integer(a, b=98):
    """
        function to add numbers
        Argumnents:
        @a: first intiger
        @b: second intiger
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
