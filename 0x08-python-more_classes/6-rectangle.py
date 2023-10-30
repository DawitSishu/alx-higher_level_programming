#!/usr/bin/python3
"""
this module is a represtaion of rectangle clASS
"""


class Rectangle():
    """
    rectangle class
    """

    num = 0

    def __init__(self, width=0, height=0):
        """
        arguments:
            width: rectangle wodth.
            height: rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.num += 1

    def __str__(self):
        """print function of the rectangle"""
        rec = ""

        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                rec += '#' * self.__width + '\n'

        return rec[:-1]

    def __repr__(self):
        """represtatuon behavior of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @property
    def width(self):
        """Gets or Sets rectangle wodth."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Gets or Sets rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of the rectangle"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __del__(self):
        """delete the rectangle"""
        Rectangle.num -= 1
        print("Bye rectangle...")
