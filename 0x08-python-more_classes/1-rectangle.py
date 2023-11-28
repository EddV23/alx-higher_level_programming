#!/usr/bin/python3
"""
Module that creates an empty class Rectangle that defines a rectangle by:
(based on 0-rectangle.py)
"""


class Rectangle:
    """Represents a Rectangle class used to create rectangle objects"""

    def __init__(self, width=0, height=0):
        """initializes an instance of the Rectangle class"""
        """self.width = width"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter method to retrieve the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
