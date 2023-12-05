#!/usr/bin/python3
"""
Module that defines a script that reads stdin line
by line and computes metrics:
"""
import sys


def print_metrics(total_size, status_codes):
    """
    Print metrics including total file size and lines by status code.
        """
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))


def generate_lines():
    """
            Generate lines from stdin and compute metrics.
                """
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    try:
        for i, line in enumerate(sys.stdin, 1):
            parts = line.split()
            if len(parts) > 2 and parts[-2] in status_codes:
                total_size += int(parts[-1])
                status_codes[parts[-2]] += 1
            if i % 10 == 0:
                print_metrics(total_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    generate_lines()
