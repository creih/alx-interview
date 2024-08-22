#!/usr/bin/python3
"""task 0 module about utf8 validation"""


def validUTF8(data):
    """validates if a list of integers represents a valid UTF-8 encoding"""
    num_bytes = 0

    for num in data:
        bin_repr = format(num, '#010b')[-8:]

        if num_bytes == 0:
            if bin_repr[0] == '0':
                continue
            elif bin_repr[:3] == '110':
                num_bytes = 1
            elif bin_repr[:4] == '1110':
                num_bytes = 2
            elif bin_repr[:5] == '11110':
                num_bytes = 3
            else:
                return False
        else:
            if bin_repr[:2] != '10':
                return False
            num_bytes -= 1

    return num_bytes == 0
