#!/usr/bin/python3
"""
a module that has a function to turn file to json represeatation
"""
import json


def to_json_string(my_obj):
    """a function to give json reprenstation of an object"""
    return json.dumps(my_obj)
