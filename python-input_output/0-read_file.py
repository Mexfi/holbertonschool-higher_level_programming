#!/usr/bin/python3
"""
This module provides a function for reading and printing
the contents of a UTF-8 text file to stdout.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.
                        Defaults to an empty string.

    Notes:
        - Uses the `with` statement for proper file handling.
        - Does not handle exceptions for missing files
          or permission issues, as required.
        - Prints the file content exactly as it appears.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
