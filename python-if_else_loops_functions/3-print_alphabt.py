#!/usr/bin/python3
for char_code in range(97, 123):
    if char_code != 101 and char_code != 113:
        print("{:c}".format(char_code), end="")
