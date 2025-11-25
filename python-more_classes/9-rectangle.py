#!/usr/bin/python3
"""Defines a Rectangle class with additional square class method.
"""


class Rectangle:
    """Represents a rectangle with width and height.

    Class Attributes:
        number_of_instances (int): Counts current Rectangle instances.
        print_symbol: Symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the Rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the Rectangle width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the Rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the Rectangle height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
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
        """Return a recreation string for eval()."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print message when a Rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on area.

        Args:
            rect_1: first Rectangle instance
            rect_2: second Rectangle instance

        Returns:
            rect_1 if both have the same area or rect_1 is bigger,
            otherwise rect_2.

        Raises:
            TypeError: if rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with equal width and height."""
        return cls(size, size)
