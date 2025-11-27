#!/usr/bin/python3
"""
This module provides a function that appends a string
to a UTF-8 encoded text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF-8 text file and
    returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Notes:
        - The file is created if it does not exist.
        - The with statement is used for file handling.
        - No exception handling for permission or missing file
          is required as per the task instructions.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
