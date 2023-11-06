#!/usr/bin/python3
"""
module that has a list class
"""


class MyList(list):
    """a list class that ingherits from class list"""
    def __init__(self):
        """initialize tghe supper class"""
        super().__init__()

    def print_sorted(self):
        """sorted list printer"""
        print(sorted(self))
