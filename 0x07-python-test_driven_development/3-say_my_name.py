#!/usr/bin/python3
"""
this module has a say my name function
"""


def say_my_name(first_name, last_name=""):
    """
    prints my name is and the supplied name
    Args:
        @first_name: first name.
        @last_name: last name.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
