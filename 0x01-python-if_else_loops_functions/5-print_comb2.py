#!/usr/bin/python3
separator = ", "
for i in range(0, 100):
    if i < 10:
        print("{}{}".format(0, i), end=separator)
    else:
        if i == 99:
            separator = "\n"
        print(i, end=separator)
