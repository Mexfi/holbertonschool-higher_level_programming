#!/usr/bin/python3
import random

number = random.randint(-100, 100) # Do not touch this line

# Complete the source code from here
print(number)
if number > 0:
    print("is positive")
elif number < 0:
    print("is negative")
else:
    print("is zero")
