#!/usr/bin/python3
"""
a module with function to read file names
"""


def read_file(filename=""):
    """function to read and print the contents of file"""
    with open(filename, encoding="utf-8") as fle:
        print(fle.read(), end="")
