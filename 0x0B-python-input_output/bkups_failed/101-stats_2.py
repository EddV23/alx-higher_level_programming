#!/usr/bin/python3
"""
Module that defines a script that reads stdin line
by line and computes metrics:
"""
import sys


def print_metrics(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def main():
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404":
                    0, "405": 0, "500": 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            if len(data) > 2:
                total_size += int(data[-1])
                code = data[-2]
                if code in status_codes:
                    status_codes[code] += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)

if __name__ == "__main__":
    main()
