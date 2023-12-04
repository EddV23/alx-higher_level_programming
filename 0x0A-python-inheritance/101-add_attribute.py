#!/usr/bin/python3
"""
Modules that defines a function that adds a
new attribute to an object if it’s possible
"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if it's possible."""
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
