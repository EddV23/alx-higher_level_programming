#!/usr/bin/python3
"""
does exactly the same as a specific
Python bytecode
does exactly the same as a specific Python bytecode
"""

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                resutlt += (a ** b) / i
        except Exception:
            result = b + a
            break
    return result
