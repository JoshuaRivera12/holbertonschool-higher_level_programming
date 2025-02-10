#!/usr/bin/python3
"""Defines BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
