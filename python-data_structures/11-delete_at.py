#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.
    If the sentence is empty, first character is None.
    """
    first_char = sentence[0] if sentence else None
    return (len(sentence), first_char)


def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.
    If idx is negative or out of range, nothing is changed.
    """
    if 0 <= idx < len(my_list):
        my_list[:] = my_list[:idx] + my_list[idx+1:]
    return my_list
