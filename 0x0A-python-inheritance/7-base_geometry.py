#!/usr/bin/python3
"""
basegeometry class with area method
"""


class BaseGeometry():
    """a class of BaseGeometry"""

    def area(self):
        """exception raiser function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """cheacks if the given value is an intiger"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
