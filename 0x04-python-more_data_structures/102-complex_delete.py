#!/usr/bin/python3
"""
deletes keys with a specific value in a dictionary
"""


def complex_delete(a_dictionary, value):
    """
    [a_dictionary.pop(key) for key, val in list(a_dictionary.items())
if val == value]
    return a_dictionary
    """
    for key, val in list(a_dictionary.items()):
        if val == value:
            a_dictionary.pop(key)
    return a_dictionary
