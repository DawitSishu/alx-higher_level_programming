#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum_total = 0
        weight = 0
        for i, j in my_list:
            sum_total += i * j
            weight += j
        if weight == 0:
            return 0
        return sum_total / weight
    return 0
