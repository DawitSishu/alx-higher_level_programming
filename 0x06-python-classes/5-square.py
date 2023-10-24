#!/usr/bin/python3
"""
This module includes a class that specifies a square,
its size, checks that the values provided are correct, and
has setter and getter methods for setting and retrieving the square.
Another method that handles the square's print is the area method, which
returns the square's area.
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

    def my_print(self):
        """Prints the square with the # character"""
        if self.__size > 0:
            for i in range(self.__size):
                print('#' * self.__size)
        else:
            print()
