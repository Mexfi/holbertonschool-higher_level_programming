#!/usr/bin/python3
"""
This module provides a function that converts a JSON string
into a corresponding Python object.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON-formatted string.

    Returns:
        The Python data structure represented by the JSON string.

    Notes:
        - No exception handling is required if the string does not
          represent a valid JSON object (json.loads will raise
          its own exception).
    """
    return json.loads(my_str)
