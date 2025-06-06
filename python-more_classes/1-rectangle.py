#!/usr/bin/python3
"""Define a Rectangle class with width and height attributes."""


class Rectangle:
    """this class defines a rectangle with width and height attributes."""
    def __init__(self, width=0, height=0):
        """Initialize the rectangle with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

