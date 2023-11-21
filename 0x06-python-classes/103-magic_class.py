#!/usr/bin/python3
"""
does exactly the same as a specific
Python bytecode
used for disassemhly of given bytecode
"""
import math


class MagicClass:
    """represents a Magic class"""
    def __init__(self, radius=0):
        """initializes an instance of the Mgic class"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """calculates and returns the area of the Magic class"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """calculates and returns the circumference of the Magic class"""
        return 2 * math.pi * self.__radius
