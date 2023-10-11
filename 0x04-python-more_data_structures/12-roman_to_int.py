#!/usr/bin/python3
def roman_to_int(roman_string):
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    final_num = 0
    prev = 0
    if type(roman_string) is str and roman_string:
        for char in roman_string:
            cur = digits[char]
            if cur > prev:
                final_num += cur - 2 * prev
            else:
                final_num += cur
            prev = cur
    return final_num
