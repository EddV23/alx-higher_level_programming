#!/usr/bin/python3
"""
Module that defines a class that inherits from list
"""


class MyList(list):
    """Inherits from list and provides a method to print the sorted list."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
