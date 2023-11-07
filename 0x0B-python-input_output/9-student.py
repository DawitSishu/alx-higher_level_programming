#!/usr/bin/python3
"""
a module with a stiudent class
"""


class student:
    """a class representation of student"""
    def __init__(self, first_name, last_name, age):
        """
        arguments:
            first_name: student first name
            last_name: student last name
            age : student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retuns a dictionary representation of the student"""
        return self.__dict__
