#!/usr/bin/python3
"""
Module that defines a class BaseGeometry (based on 5-base_geometry.py)
"""


class BaseGeometry:
    """Empty class with an area method that raises an Exception."""

    def area(self):
        """Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")
