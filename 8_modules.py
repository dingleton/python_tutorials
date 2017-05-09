# -*- coding: utf-8 -*-
"""
Code to test the  import functions from a separate python file fib_mod.py

Two functions are imported and called.
The first prints the Fibonnaci to a max of value
The second to returns a list of fibonnaci value to a max value

"""

from fib_mod import fib_print, fib_return

#call a function to print fibonnaci series from 1 to  max of 50
max_fib = 50
fib_print(max_fib)

#assign a variable name to an external function and print fibonnaci series 1 to max 100#
max_fib = 100
f1 = fib_print
f1(max_fib)

#return and print a list of fibonnaci series from 1 to 1,000 
max_fib = 1000
print('Fibonnci series from 1 to max of {} : {}'.format(max_fib, fib_return(max_fib)))
