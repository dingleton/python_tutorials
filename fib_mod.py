# -*- coding: utf-8 -*-
"""

Sample code for modules in chapter 8 of the Python tutorial
These incluse functions to print & return Fibonnci series

"""

def fib_print(max):
    """ Module to print fibonnaci series from 0 to n (inclusive)
    """
    a, b = 0, 1
    print('Fibonnci series from 1 to max of {} :'.format(max), end=' ')
    while b <= max:
        print(b, end=' ')
        a, b = b, a+b
    print("\n")

def fib_return(max):
    """ Module to return a string of a fibbonacci series from 0 to n (inclusive)
    """
    result = []
    c, d = 0, 1
    while d <= max:
        result.append(d)
        c, d = d, c+d
    return result
    