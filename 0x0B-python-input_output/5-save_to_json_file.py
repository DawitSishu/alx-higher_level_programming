#!/usr/bin/python3
"""
a module that has a function to write json on file
"""
import json


def save_to_json_file(my_obj, filename):
    """a function to write a json represntation of file"""
    with open(filename, "w") as fle:
        json.dump(my_obj, fle)
