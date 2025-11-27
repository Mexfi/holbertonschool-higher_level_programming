#!/usr/bin/python3
"""
This module provides a function that creates a Python object
from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        The Python object represented by the JSON content.

    Notes:
        - Uses the with statement.
        - Does not handle exceptions for bad JSON or file issues.
        - json.load() and open() naturally raise exceptions as required.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
