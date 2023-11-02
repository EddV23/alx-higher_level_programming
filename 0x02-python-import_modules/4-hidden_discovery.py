#!/usr/bin/python3

"""
program that prints all the names defined
by the compiled module hidden_4.pyc
(https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc)
"""

import hidden_4

if __name__ == "__main__":
    """file = dir(hidden_4)"""
    for name in dir(hidden_4):
        if name[0:2] != "__":
            print(name)
