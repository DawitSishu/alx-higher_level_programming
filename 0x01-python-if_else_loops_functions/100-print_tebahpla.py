#!/usr/bin/python3
separator = ""
for i in reversed(range(97, 123)):
    if (i % 2) == 0:
        separator += chr(i)
    else:
        separator += chr(i-32)
print("{}".format(separator), end="")
