#!/usr/bin/python3
class Rectangle:
    # Public class attributes
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        # Instance attributes
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # Property for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # Property for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Method to compute area
    def area(self):
        return self.width * self.height

    # Method to compute perimeter
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    # Method for string representation
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return str(self.print_symbol) * self.width + "\n" * (self.height - 1) + str(self.print_symbol) * self.width

    # Method for formal string representation for eval()
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    # Destructor method
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")


