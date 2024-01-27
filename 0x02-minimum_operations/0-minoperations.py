#!/usr/bin/python3
"""Minimum operations"""
from math import sqrt


def minOperations(n):
    """ Find minmum number of operations needed to have
    n numbers of H in the file
    """
    if n == 1:
        return 0
    no = 0
    fac = 2
    while fac <= n:
        if n % fac == 0:
            n //= fac
            no += fac
        else:
            fac += 1
    return no
