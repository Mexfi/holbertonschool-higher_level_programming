#!/usr/bin/python3
"""
Module: 11-square
Contains class Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle"""

    def __init__(self, size):
        """
        Initialize Square with size

        Args:
            size: size of square (positive integer)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the square description: [Square] <size>/<size>"""
        return "[Square] {}/{}".format(self.__size, self.__size)
