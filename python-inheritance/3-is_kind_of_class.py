#!/usr/bin/python3
"""
Module: 3-is_kind_of_class
Contains function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an 
    instance of a class that inherited from, the specified class; 
    otherwise False.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        bool: True if obj is instance of a_class or its subclass, False otherwise
    """
    return isinstance(obj, a_class)
