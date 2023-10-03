#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for s in str:
        if ord(s) > 96 and ord(s) < 123:
            upper_str += chr(ord(s)-32)
        else:
            upper_str += s
    print("{}".format(upper_str))
