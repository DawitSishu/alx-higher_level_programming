#!/usr/bin/python3
"""
a module with a stiudent class
"""


class Student:
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

    def to_json(self, attrs=None):
        """
        arguments:
            attrs: optional attributes to be represented
        """
        if isinstance(attrs, list) and all(isinstance(el, str)for el in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        arguments:
            json: the diction to replace the vlues with
        """
        for key, val in json.items():
            setattr(self, key, val)
