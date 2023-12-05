#!/usr/bin/python3
"""
Module that defines a script that reads stdin line
by line and computes metrics:
"""


def print_metrics(total_size, status_codes):
    """
    Print metrics including total file size and lines by status code.
    "
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))
    """
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))


if __name__ == "__main__":
    import sys

    """
    Generate lines from stdin and compute metrics.
    """
    total_size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_metrics(total_size, status_codes)
                count = 1
            else:
                count += 1

            parts = line.split()

            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if parts[-2] in valid_codes:
                    if status_codes.get(parts[-2], -1) == -1:
                        status_codes[parts[-2]] = 1
                    else:
                        status_codes[parts[-2]] += 1
            except IndexError:
                pass

        print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise
