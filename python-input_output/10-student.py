#!/usr/bin/python3
"""
This module defines a Student class with attributes first_name,
last_name, and age, and a method to return its dictionary
representation for JSON serialization.
"""


class Student:
    """
    Defines a student with first name, last name, and age.

    Public instance attributes:
        - first_name (str)
        - last_name (str)
        - age (int)
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

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
        Returns a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to include.
                                    If None or not a list, all attributes
                                    are included.

        Returns:
            dict: Dictionary containing the requested attributes.
        """
        if isinstance(attrs, list):
            return {key: value for key, value in self.__dict__.items()
                    if key in
