#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list, handling IndexError if x is too large.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print.

    Returns:
        int: The real number of elements printed.
    """
    printed_count = 0
    try:
        # Loop up to x elements. Since we cannot use len(), we rely on
        # the IndexError exception to detect the list boundary.
        for i in range(x):
            # Attempt to access the element and print it without a newline
            print(my_list[i], end="")
            printed_count += 1
    except IndexError:
        # This block executes if i becomes greater than or equal to the
        # length of my_list (i.e., x was too big).
        # We don't need to do anything here except break the printing process.
        pass
    
    # Print the final newline character as required by the prototype
    # (after all elements have been printed, regardless of success or exception).
    print()

    # Return the actual number of elements successfully printed
    return printed_count

# Example usage (for testing purposes):
if __name__ == "__main__":
    my_list_1 = [1, 2, 3, 4, 5]
    
    nb_print = safe_print_list(my_list_1, 2)
    print("Nb elements printed: {}".format(nb_print))
    
    nb_print = safe_print_list(my_list_1, len(my_list_1)) # Note: Using len() only in the test case for comparison
    print("Nb elements printed: {}".format(nb_print))
    
    nb_print = safe_print_list(my_list_1, 10)
    print("Nb elements printed: {}".format(nb_print))
    
    my_list_2 = [1, "test", 5.5, True]
    nb_print = safe_print_list(my_list_2, 3)
    print("Nb elements printed: {}".format(nb_print))
