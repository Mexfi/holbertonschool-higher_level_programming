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

    def to_json(self):
        """
        Returns a dictionary representation of the Student instance.

        Returns:
            dict: Dictionary containing all public attributes.
        """
        return self.__dict__.copy()
