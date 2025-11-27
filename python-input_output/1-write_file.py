#!/usr/bin/python3
"""
This module provides a function that writes a string
to a UTF-8 encoded text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 text file and returns
    the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write into the file.

    Notes:
        - The file is created if it does not exist.
        - The file content is overwritten if it already exists.
        - The with statement is used for file handling.
        - No file permission exception handling is required.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
