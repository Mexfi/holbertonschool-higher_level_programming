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
        sorted_list = self.copy()  # Create a copy to avoid modifying original
        sorted_list.sort()         # Sort the copy
        print(sorted_list)         # Print the sorted copy
