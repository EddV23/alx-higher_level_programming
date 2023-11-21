1#!/usr/bin/python3
"""
a class Square that defines a square by: (based on 4-square.py)
"""


class Square:
    """represents a square"""
    def __init__(self, size=0):
        """initializes an instance of the Square class"""
        self.__size = size
        self.__validate_size()

    @property
    def size(self):
        """Getter method to retrieve the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute"""
        self.__size = value
        self.__validate_size()

    def __validate_size(self):
        """validates the size attribute."""
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """calculates and returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints the square using the '#' character"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
