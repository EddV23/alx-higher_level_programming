#!/usr/bin/python3
"""
Module that defines a class Square that
inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle with overridden str method."""

    def __init__(self, size):
        """Instantiates with size, validates it."""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the square description."""
        return ("[Square] {}/{}".format(self.__size, self.__size))
