#!/usr/bin/python3

"""
imports functions from the file calculator_1.py,
handles basic operations
"""
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argv = sys.argv
    length = len(argv) - 1
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))
