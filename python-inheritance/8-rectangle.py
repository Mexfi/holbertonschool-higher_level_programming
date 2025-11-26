#!/usr/bin/python3
"""
Module: 8-rectangle
Contains class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        Initialize Rectangle with width and height

        Args:
            width: width of rectangle (positive integer)
            height: height of rectangle (positive integer)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
