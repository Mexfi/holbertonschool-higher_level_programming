#!/usr/bin/python3
"""
Module: 1-my_list
Contains class MyList that inherits from list
"""


class MyList(list):
    """
    A class that inherits from list with additional functionality
    """
    
    def print_sorted(self):
        """
        Prints the list sorted in ascending order
        Does not modify the original list
        """
        if all(isinstance(x, int) for x in self):
            sorted_list = sorted(self)
            print(sorted_list)
        else:
            print("All elements must be integers")
