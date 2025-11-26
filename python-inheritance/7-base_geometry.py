#!/usr/bin/python3
"""
Module: 7-base_geometry
Contains class BaseGeometry with area and integer_validator methods
"""


class BaseGeometry:
    """A class BaseGeometry with area and integer_validator methods"""

    def area(self):
        """Raises an Exception with message 'area() is not implemented'"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value

        Args:
            name (str): The name of the parameter
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
