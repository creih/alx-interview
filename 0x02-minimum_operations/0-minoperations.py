#!/usr/bin/python3
"""this file is to minimise nbr of ops to copy a letter given nbr of times"""


def minOperations(n):
    """method to make the calculation of least times"""
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations
