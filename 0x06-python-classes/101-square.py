#!/usr/bin/python3
"""
This module includes a class that specifies a square's dimensions
and location on the screen, checks that the values provided are
accurate, and provides setter and getter methods for changing the
parameters. To manage the use of the built-in print function, there
is a __str__ method here. Another method that handles the square's
print is the area method, which returns the square's area.
"""


class Square():
    """Defines the Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Attributes:
            size (int): the size of length ofthe square.
            position (tuple): coordinates of the square.
        """
        self.size = size
        self.position = position

    def __str__(self):
        """Sets the print behavior of  Square."""
        square_str = ""

        if self.__size > 0:
            for i in range(self.__position[1]):
                square_str += '\n'
            for j in range(self.__size):
                square_str += ' ' * self.__position[0]
                square_str += '#' * self.__size + '\n'

        return square_str[:-1]

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

    @property
    def position(self):
        """Get or set coordinate positions."""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) is 2 and \
                type(value[0]) is int and type(value[1]) is int:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the # character"""
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
