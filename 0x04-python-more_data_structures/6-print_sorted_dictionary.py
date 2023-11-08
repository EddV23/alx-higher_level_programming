#!/usr/bin/python3
"""
prints a dictionary by ordered keys
"""


def print_sorted_dictionary(a_dictionary):
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
    """
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
        """print(f"{key}: {a_dictionary[key]}")"""
