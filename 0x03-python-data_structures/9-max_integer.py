#!/usr/bin/python3
"""
finds the biggest integer of a list
"""


def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max_num = my_list[0]
        for i in my_list:
            if i > max_num:
                max_num = i
        return max_num
