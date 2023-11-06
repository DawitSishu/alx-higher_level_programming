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
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
