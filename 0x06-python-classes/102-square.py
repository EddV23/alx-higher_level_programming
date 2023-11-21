#!/usr/bin/python3
"""
a class Square that defines a square by: (based on 4-square.py)
"""


class Square:
    """represents a square"""
    def __init__(self, size=0):
        """initializes an instance of the Square class"""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates and returns the area of the square"""
        return self.__size ** 2

    def __eq__(self, other):
        """equality comparison"""
        return self.area() == other.area()

    def __ne__(self, other):
        """inequality comparison"""
        return self.area() != other.area()

    def __lt__(self, other):
        """less than comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """less than or equal to comparison"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """greater than comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """greater than or equal to comparison"""
        return self.area() >= other.area()
