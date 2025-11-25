#!/usr/bin/python3
"""Class MyList that inherits from list and has a method to print a sorted list."""

class MyList(list):
    """Inherits from the built-in list class."""

    def print_sorted(self):
        """Prints the list, but sorted in ascending order."""
        print(sorted(self))
