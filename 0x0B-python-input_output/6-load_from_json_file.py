#!/usr/bin/python3
"""
a module that has a function to read json from file
"""
import json


def load_from_json_file(filename):
    """function that reads the json from a file"""
    with open(filename) as fle:
        return json.load(fle)
