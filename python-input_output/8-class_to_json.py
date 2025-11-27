#!/usr/bin/python3
"""
This module provides a function that returns the dictionary
description of a class instance for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of a class instance.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing all attributes of the object,
              including private attributes, with values that are
              serializable (list, dict, str, int, bool).
    """
    return obj.__dict__.copy()
