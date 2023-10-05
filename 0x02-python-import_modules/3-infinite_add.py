#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    i = 0
    for val in sys.argv:
        if i > 0:
            result += int(val)
        i += 1
    print(result)
