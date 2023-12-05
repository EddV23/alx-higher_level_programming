#!/usr/bin/python3
"""
Module that defines a function that inserts a
line of text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each
    line containing a specific string.
    """
    with open(filename, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i + 1, new_string)
        file.seek(0)
        file.writelines(lines)
