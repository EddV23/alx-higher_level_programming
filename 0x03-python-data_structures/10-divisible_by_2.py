#!/usr/bin/python3
"""
finds all multiples of 2 in a list
"""


def divisible_by_2(my_list=[]):
    """
    return [True if i % 2 == 0 else False for i in my_list]
    or
    """

    """if len(my_list) == 0:"""
    if not my_list:
        return None

    mul_2_list = []
    for i in my_list:
        if i % 2 == 0:
            mul_2_list.append(True)
        else:
            mul_2_list.append(False)

    return mul_2_list
