#!/usr/bin/python3
"""
Module that defines a class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry:
    """Class with an integer validator method."""

    def area(self):
        """Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        "
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        """
