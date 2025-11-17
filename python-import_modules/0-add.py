#!/usr/bin/python3
def add(a, b):
    return a + b

if __name__ == "__main__":
    # This block will not be executed when imported
    pass

from add_0 import add

a = 1
b = 2

print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
