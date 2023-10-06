#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print()
        return
    for row in matrix:
        for idx, col in enumerate(row):
            if idx == len(row) - 1:
                print("{}".format(col), end="")
            else:
                print("{}".format(col), end=" ")
        print()
