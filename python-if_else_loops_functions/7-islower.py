#!/usr/bin/env python3
def islower(c):
    """Check if a character is lowercase."""
    if len(c) != 1:
        return False  # Optional: only consider single characters
    return 97 <= ord(c) <= 122
