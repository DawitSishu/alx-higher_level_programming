#!/usr/bin/python3
separator = ", "
for i in range(0, 100):
    number_1 = i % 10
    number_2 = i / 10
    if i < 10 and number_2 < number_1:
        print("{}{}".format(0, i), end=separator)
    elif number_2 < number_1:
        if i == 89:
            separator = "\n"
        print(i, end=separator)
