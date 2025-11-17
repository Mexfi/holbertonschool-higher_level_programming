#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Checks if each integer in a list is a multiple of 2.

    Args:
        my_list: A list of integers.

    Returns:
        A new list of booleans, where True indicates the corresponding
        integer is a multiple of 2, and False otherwise.
        The new list has the same size as the original list.
    """
    result_list = []
    for number in my_list:
        if number % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list
