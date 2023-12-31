#!/usr/bin/python3
"""
Modules that defines a class Student that defines
a student by the Public instance attributes
first_name, last_name and age
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        return self.__dict__
