#!/usr/bin/python3
"""
a module with function to write on files
"""


def write_file(filename="", text=""):
    """
    arguments:
        filename: name of file
        text: text to be written
    Returns:
        written number of characters
    """
    with open(filename, "w", encoding="utf-8") as fle:
        return fle.write(text)
