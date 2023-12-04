#!/usr/bin/python3
"""
Module that defines a class Rectangle that inherits
from BaseGeometry (7-base_geometry.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Instantiates with width and height, validates them.

        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
