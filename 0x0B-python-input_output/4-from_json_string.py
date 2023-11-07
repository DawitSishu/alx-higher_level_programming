#!/usr/bin/python3
"""
a module that has a function to turn json to object
"""
import json


def from_json_string(my_str):
    """a funnction that give objeect representation of an object"""
    return json.loads(my_str)
