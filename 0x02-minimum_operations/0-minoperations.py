#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """
        args: n
        Return: an integer
    """
    if n <= 1:
        return 0
    for opr in range(2, n+1):
        if n % opr == 0:
            return minOperations(int(n/opr)) + opr
