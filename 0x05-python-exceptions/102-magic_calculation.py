#!/usr/bin/python3

def magic_calculation(a, b):
    final = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception('Too far')
            else:
                final += (a ** b) / i
        except Exception:
            final = a + b
            break
    return final
