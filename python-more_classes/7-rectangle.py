#!/usr/bin/python3
"""Defines a Rectangle class for Holberton project 7-rectangle.
"""


class Rectangle:
    """Represents a rectangle with width and height.

    Class Attributes:
        number_of_instances (int): counts active instances.
        print_symbol: symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set rectangle height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return printable rectangle using print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""

        row = str(self.print_symbol) * self.width
        return "\n".join([row for _ in range(self.height)])

    def __repr__(self):
        """Return eval()-recreatable string."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print message when instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
