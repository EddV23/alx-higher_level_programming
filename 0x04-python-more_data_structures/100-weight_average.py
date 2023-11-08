#!/usr/bin/python3
"""
returns the weighted average of all integers tuple (<score>, <weight>)
"""


def weight_average(my_list=[]):
    """
    if not my_list:
        return 0
    return sum(score * weight for score, weight in my_list) / sum(weight for _, weight in my_list)
    """
    if not my_list:
        return 0

    sum_scores = 0
    sum_weights = 0

    for score, weight in my_list:
        sum_scores += score * weight
        sum_weights += weight

    if sum_weights == 0:
        return 0

    return sum_scores / sum_weights
