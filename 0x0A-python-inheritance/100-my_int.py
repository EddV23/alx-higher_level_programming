#!/usr/bin/python3
"""
Module that defines a class MyInt that inherits from int
"""


class MyInt(int):
    """MyInt class inheriting from int with inverted == and != operators."""

    def __eq__(self, other):
        """Inverts the == operator."""
        # return int(self) != int(other)
        # return self.real != other
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the != operator."""
        # return int(self) == int(other)
        # return self.real == other
        return super().__eq__(other)
