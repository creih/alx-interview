#!/usr/bin/python3
"""Requirements
General

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the PEP 8 style (version 1.7.x)
    All your files must be executable
    The length of your files will be tested using wc

Tasks
0. Log parsing
mandatory

Write a script that reads stdin line by line and computes metrics:

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
    After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
        Total file size: File size: <total size>
        where <total size> is the sum of all previous <file size> (see input format above)
        Number of lines by status code:
            possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            if a status code doesn’t appear or is not an integer, don’t print anything for this status code
            format: <status code>: <number>
            status codes should be printed in ascending order
"""
import sys
import signal
import re


def print_stats(status_codes, total_size):
    """printing the stats of  a log file"""
    status_codes = {}
    print("File size: {}".format(total_size))
    for k in sorted(status_codes.keys()):
        if status_codes[k] != 0:
            print("{}: {}".format(k, status_codes[k]))
    return


def signal_handler(sig, frame):
    """handling the signal"""
    print_stats(status_codes, total_size)


def parse_line(line):
    """parsing the line"""
    try:
        split_line = line.split(" ")
        file_size = int(split_line[-1])
        status_code = int(split_line[-2])
        if status_code in status_codes.keys():
            status_codes[status_code] += 1
        total_size[0] += file_size
    except Exception:
        pass


if __name__ == "__main__":
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    total_size = [0]
    signal.signal(signal.SIGINT, signal_handler)
    line_count = 0
    try:
        for line in sys.stdin:
            parse_line(line)
            line_count += 1
            if line_count == 10:
                print_stats(status_codes, total_size[0])
                line_count = 0
    except KeyboardInterrupt:
        print_stats(status_codes, total_size[0])
        raise
    print_stats(status_codes, total_size[0])
