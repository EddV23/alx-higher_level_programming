#!/usr/bin/python3
"""
 returns the number of keys in a dictionary
"""


def number_keys(a_dictionary):
    """
    return len(a_dictionary)
    """
    count = 0
    for key in a_dictionary:
        count += 1
    return count
