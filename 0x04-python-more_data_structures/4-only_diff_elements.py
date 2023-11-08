#!/usr/bin/python3
"""
returns a set of all elements present in only one set
"""


def only_diff_elements(set_1, set_2):
    """
    return set_1 ^ set_2
    """
    diff_set = set()
    for element in set_1:
        if element not in set_2:
            diff_set.add(element)
    for element in set_2:
        if element not in set_1:
            diff_set.add(element)
    return diff_set
