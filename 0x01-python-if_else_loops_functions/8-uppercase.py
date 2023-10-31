#!/usr/bin/python3
def uppercase(str):
    """
    function that prints a string in uppercase character,
    followed by a new line
    """
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("")
