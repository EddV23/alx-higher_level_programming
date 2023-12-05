#!/usr/bin/python3
"""
Modules that defines a class Student that defines a student
by: (based on 10-student.py) the Public instance attributes
first_name, last_name and age
"""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student
        instance with specific attributes.
        """
        if attrs is None:
            return self.__dict__

        result = {}
        for key in attrs:
            if hasattr(self, key):
                result[key] = getattr(self, key)

        return result
        # return {key: result[key] for key in attrs if key in result}
        """or

        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}
        """

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student
        instance with a provided dictionary.
        "
        for key, value in json.items():
            setattr(self, key, value)
        """
        self.__dict__.update(json)
