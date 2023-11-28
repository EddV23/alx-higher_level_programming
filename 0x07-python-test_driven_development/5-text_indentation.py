#!/usr/bin/python3
"""
Module for printing text with 2 new lines after ., ? and : characters.


"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after ., ? and : characters.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    current_line = True
    for char in text:
        if not (char == ' ' and current_line):
            print(char, end='')
            current_line = False
            if char in separators:
                print('\n')
                current_line = True
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']

    lines = []
    current_line = ""
    for char in text:
        current_line += char
        if char in separators:
            lines.append(current_line.strip())
            lines.append("")  # Two new lines
            current_line = ""

    if current_line.strip():
        lines.append(current_line.strip())

    print("\n".join(lines))
    """
