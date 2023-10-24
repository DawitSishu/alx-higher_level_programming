#!/usr/bin/python3
"""Square module.
This module has a class that defines a square.
"""


class Square():
    """Defines a square."""

    def __init__(self, size):
        """
        Args:
            size (int): the size of one edge of the square.
        """
        self.__size = size
