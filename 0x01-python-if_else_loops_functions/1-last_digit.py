#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
remained = number % 10
if remained > 5:
    print(f"Last digit of {number} is {remained} and is greater than 5")
elif remained == 0:
    print(f"Last digit of {number} is 0 and is 0")
else:
    print(f"Last digit of {number} is {remained} and is less than 6 and not 0")
