#!/usr/bin/python3
"""
converts a Roman numeral to an integer
"""


def roman_to_int(roman_string):
    rom_str = roman_string

    if not isinstance(rom_str, str) or not rom_str:
        return 0
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(rom_str)):
        if i > 0 and rom_num[rom_str[i]] > rom_num[rom_str[i - 1]]:
            result += rom_num[rom_str[i]] - 2 * rom_num[rom_str[i - 1]]
        else:
            result += rom_num[rom_str[i]]
    return result
    """
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    rom_nm = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman_string)):
        if i > 0 and rom_nm[roman_string[i]] > rom_nm[roman_string[i - 1]]:
            result += rom_nm[roman_string[i]] - 2 * rom_nm[roman_string[i - 1]]
        else:
            result += rom_nm[roman_string[i]]
    return result
    """
