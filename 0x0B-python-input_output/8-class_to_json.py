#!/usr/bin/python3
"""
a module to define a python class to json fucntion
"""


def class_to_json(obj):
    """a functionto return a json repreentation of an object"""
    return obj.__dict__
