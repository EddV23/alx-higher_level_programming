#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv = sys.argv
    length = len(argv) - 1

    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
    else:
        print("{:d} arguments".format(length))

    for i in range(1, length + 1):
        print("{:d}: {:d}".format(i, argv[i]))
