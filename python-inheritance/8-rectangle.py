#!/usr/bin/python3
"""
Class BaseGeometry
Class Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Superclass import """


class Rectangle(BaseGeometry):
    """Class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        """Expose integer_validator to make it appear in dir(Rectangle)"""
        return super().integer_validator(name, value)
