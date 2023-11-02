#!/usr/bin/python3

"""
program that prints the results of
the addition of all of arguments
"""
import sys

if __name__ == "__main__":
    argv = sys.argv
    length = len(argv) - 1
    """length = len(argv)"""
    result = 0

    for i in range(1, length + 1):
        result += int(argv[i])
    print("{:d}".format(result))
    """
    length = len(argv)
    for i in range(1, length)
        result += int(argv[i])
    print("{:d}".format(result))
    or
    for i in range(0, length - 1):
        result += int(argv[i + 1])
    print("{:d}".format(result))
    """
