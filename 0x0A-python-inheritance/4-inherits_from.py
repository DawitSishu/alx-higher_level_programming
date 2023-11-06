#!/usr/bin/python3
"""
modlue with class for comparison
"""


def inherits_from(obj, a_class):
    """
    returns if an objec is one that inherits
    from a class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
