#!/usr/bin/python3
"""
for i in range(122, 96, -1):
    print("{:c}".format(i if i % 2 == 0 else i - 32), end="")
"""

for i in range(122, 96, -1):
    if (122 - i) % 2 != 0:
        i = i - 32
    print("{}".format(chr(i)), end="")

"""
for i in reversed(range(97, 123)):
    if i % 2 != 0:
        i = i - 32
    print("{}".format(chr(i)), end="")
"""
