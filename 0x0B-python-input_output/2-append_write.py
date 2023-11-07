#!/usr/bin/python3
"""
a module with function to write on files
"""


def append_write(filename="", text=""):
    """
    arguments:
        filename: name of file
        text: text to be appended
    Returns:
        appended number of characters
    """
    with open(filename, "a", encoding="utf-8") as fle:
        return fle.write(text)
