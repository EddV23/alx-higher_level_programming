#!/usr/bin/python3
"""
returns a tuple with the length of a
string and its first character
"""


def multiple_returns(sentence):
    if len(sentence) != 0:
        return (len(sentence), sentence[0])
    else:
        return (len(sentence), None)
    """
    length = len(sentence)
    if length == 0:
        first = None
    else:
        first = sentence[0]
    return length, first
    """
