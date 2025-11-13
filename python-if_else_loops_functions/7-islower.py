#!/usr/bin/python3
def islower(c):
    """Check if a character is lowercase"""
    ascii_val = ord(c)
    return 97 <= ascii_val <= 122
