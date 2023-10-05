#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    idx = 0
    totalArgs = len(sys.argv) - 1
    if totalArgs == 1:
        print("1 argument", end="")
    elif totalArgs != 1:
        print("{} arguments".format(totalArgs), end="")
    if totalArgs == 0:
        print(".")
    else:
        print(":")
    if totalArgs > 0:
        for arg in sys.argv:
            if idx > 0:
                print("{}: {}".format(idx, arg))
            idx += 1
