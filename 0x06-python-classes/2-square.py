#!/usr/bin/python3
"""
This module includes a class that specifies a square and
an init method that determines its size and verifies the
accuracy of the supplied values.
"""


class Square():
    """Defines the Square class."""

    def __init__(self, size=0):
        """
        Attributes:
            size (int): the size length the square.
        Raise:
            TypeError: if size  length is not provided as an integer.
            ValueError: if size length is less than 0.
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
