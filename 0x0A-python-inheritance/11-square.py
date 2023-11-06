#!/usr/bin/python3
"""
a module with a square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a square class inherites from rectangle class"""

    def __init__(self, size):
        """check and assign size of the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """str value setter of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
