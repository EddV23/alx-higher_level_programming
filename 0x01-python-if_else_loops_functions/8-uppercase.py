#!/usr/bin/python3

def uppercase(str):
    """
    function that prints a string in uppercase character,
    followed by a new line
    """
    upper = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        upper += i
    print("{}".format(upper))
