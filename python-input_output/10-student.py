#!/usr/bin/python3
class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to include.
                                   If None, all attributes are included.

        Returns:
            dict: Dictionary representation of the student
        """
        if attrs is None:
            # Return all attributes
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            # Return only specified attributes that exist
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
