#!/usr/bin/python3
"""
Module that defines  a class Square that
inherits from Rectangle (9-rectangle.py)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        """Instantiates with size, validates it."""
        super().__init__(size, size)
        self.__size = size
