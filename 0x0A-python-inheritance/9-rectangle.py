#!/usr/bin/python3
"""
module with reactangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a rectangle class inherites from basegeomety class"""

    def __init__(self, width, height):
        """check and assign width, and height of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """str value setter of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """a method for area of the rectangle"""
        return self.__width * self.__height
