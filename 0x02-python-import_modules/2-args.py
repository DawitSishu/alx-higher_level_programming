#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    totalArgs = len(sys.argv) - 1
    if totalArgs == 1:
        print("1 argument", end="")
    elif totalArgs != 1:
        print("{} arguments".format(totalArgs), end="")
    if totalArgs == 0:
        print(".")
    else:
        print(":")
    
