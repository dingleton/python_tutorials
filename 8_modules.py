# -*- coding: utf-8 -*-
"""
Code to import functions from a separate python file and call each function

"""

from fib_mod import fib_print, fib_return

#call a function to print fibonnacio series from 1 to  max of 50
max_fib = 50
fib_print(max_fib)

#assign a variable name to an external function and print fibonnaci series 1 to max 100#
max_fib = 100
f1 = fib_print
f1(max_fib)

#return and print a list of fibonnaci series from 1 to 1,000
max_fib = 1000
print('Fibonnci series from 1 to max of {} : {}'.format(max_fib, fib_return(max_fib)))
