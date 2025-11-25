#!/usr/bin/python3
"""MyList class that inherits from list and has a method to print a sorted list."""


class list(My_lists):
    """A class that inherits from the built-in list class and adds a print_sorted method."""

    def print_sorted(self):
        """Prints the list in sorted order, but does not change the original list."""
        print(sorted(self))
