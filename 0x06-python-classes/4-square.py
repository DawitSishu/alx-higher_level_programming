#!/usr/bin/python3
"""
This module includes a class that specifies a square,
its size, checks that the values provided are correct,
and has setter and getter methods for setting and retrieving the
square. There is a method called "area" that returns the square's area.
"""


class Square():
    """Defines the Square class."""

    def __init__(self, size=0):
        """
        Attributes:
            size (int): the size of length ofthe square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the area of the square"""

        return self.__size ** 2
