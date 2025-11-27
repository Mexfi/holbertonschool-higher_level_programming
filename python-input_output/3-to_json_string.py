#!/usr/bin/python3
"""
This module provides a function that returns the JSON
representation of a Python object.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to serialize to JSON.

    Returns:
        str: The JSON-formatted string representation of the object.

    Notes:
        - No exception handling is required if the object cannot
          be serialized (json.dumps will naturally raise an error).
    """
    return json.dumps(my_obj)
