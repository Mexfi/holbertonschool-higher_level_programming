#!/usr/bin/python3
"""
This module provides a function that writes a Python object
to a text file using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The name of the file to write to.

    Notes:
        - Uses the with statement.
        - No need to handle serialization exceptions.
        - No need to handle file permission exceptions.
        - If the object cannot be serialized, json.dumps will
          raise a TypeError naturally.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
