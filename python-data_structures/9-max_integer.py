#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return None

    # Initialize max_val with the first element of the list
    max_val = my_list[0]

    # Iterate through the rest of the list
    for num in my_list[1:]:
        if num > max_val:
            max_val = num

    return max_val
