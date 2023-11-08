#!/usr/bin/python3
"""adds all unique integers in a list (only once for each integer)"""


def uniq_add(my_list=[]):
    unique_list = []
    sum_unique = 0
    for num in my_list:
        if num not in unique_list:
            unique_list += [num]
            sum_unique += num
    return sum_unique
    """
    return sum(set(my_list))

    unique_set = set()
    sum_unique = 0
    for num in my_list:
        if num not in unique_set:
            unique_set.add(num)
            sum_unique += num
    return sum_unique

    unique_dict = {}
    sum_unique = 0
    for num in my_list:
        if num not in unique_dict:
            unique_dict[num] = True
            sum_unique += num
    return sum_unique
    """
