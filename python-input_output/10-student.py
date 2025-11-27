#!/usr/bin/python3
"""
This module defines a Student class with public attributes
first_name, last_name, and age. It provides a method to
return a dictionary representation of the instance.
"""


class Student:
    """
    Represents a student with first name, last name, and age.

    Public instance attributes:
        - first_name (str)
        - last_name (str)
        - age (int)
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the Student instance.

        If attrs is a list of strings, only the attributes
        contained in this list will be included in the result.
        Otherwise, all attributes will be included.

        Args:
            attrs (list, optional): List of attribute names to include.

        Returns:
            dict: Dictionary of the requested attrib
