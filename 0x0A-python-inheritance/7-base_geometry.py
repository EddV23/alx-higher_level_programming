#!/usr/bin/python3
"""
Module that defines a class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry:
    """Class with an integer validator method."""

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
