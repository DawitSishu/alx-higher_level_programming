#!/usr/bin/python3
"""
a module with a function that computes pascals triangle
"""


def pascal_triangle(n):
    """
    a function that computes pascals triangle using lists of lists
    """
    if n <= 0:
        return []

    lists = [[1]]
    while len(lists) != n:
        prev = lists[-1]
        temp = [1]
        for i in range(len(prev) - 1):
            temp.append(prev[i] + prev[i + 1])
        temp.append(1)
        lists.append(temp)
    return lists
