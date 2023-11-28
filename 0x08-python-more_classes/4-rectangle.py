#!/usr/bin/python3
"""
Module that creates an empty class Rectangle that defines a rectangle by:
(based on 3-rectangle.py)
"""


class Rectangle:
    """Represents a Rectangle class used to create rectangle objects"""

    def __init__(self, width=0, height=0):
        """initializes an instance of the Rectangle class"""
        self.width = width
        self.height = height

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

    def area(self):
        """calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates and returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """returns a string representation of the rectangle"""
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        result += self.__height * ("#" * self.__width + "\n")
        return result.rstrip()

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return "{}({}, {})".format(type(self).__name__, self.width,
                                   self.height)
