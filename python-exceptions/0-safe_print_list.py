#!/usr/bin/python3
"""
Function to safely print x elements of a list.
"""

def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list, handling IndexError if x is too large.

    Args:
        my_list (list): The list to print elements from.
        x (int): The maximum number of elements to print.

    Returns:
        int: The actual number of elements printed.
    """
    
    # Initialize a counter for the number of elements successfully printed
    printed_count = 0
    
    # We iterate up to x times, checking if the index is valid inside the try block
    # We use range(x) to adhere to the constraint of not using len() on my_list
    for i in range(x):
        try:
            # Attempt to access the element at index i and print it
            # The end="" argument ensures all elements are on the same line
            print(my_list[i], end="")
            
            # If successful, increment the count
            printed_count += 1
            
        except IndexError:
            # This block executes if i is greater than or equal to the list's length
            # Since we hit the end of the list, we stop printing immediately
            break
            
    # Print a newline character after all elements have been printed
    print("")
    
    # Return the real number of elements that were successfully printed
    return printed_count
