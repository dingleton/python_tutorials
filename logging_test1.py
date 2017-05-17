# -*- coding: utf-8 -*-
"""
Sample python code to tes/experiment with the logging function

"""
#Logging levels
#DEBUG - Detailed infor , useful for debugging code/diagnosing problems

#INFO - Confirmation things are working as expected

#WARNING - An indication something unexpected has happened or an indiction of
#some problem in the near future e.g. disk space low. Code is still working as 
#expected. This is the default level

#ERROR - A more serious problem, the software has not been able to perform some
#function

#CRITICAL - A serious error. The program may not be able to continue running

#See https://docs.python.org/3/howto/logging.html for more info

import logging

logging.basicConfig(filename='logging_test1.log',
                    level=logging.DEBUG, 
                    format='%s(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    """Add function"""
    return x + y

def subtract(x, y):
    """Subtract function"""
    return x - y

def multiply(x, y):
    """multiply function"""
    return x * y

def divide(x, y):
    """divide function"""
    return x / y

num1 = 10
num2 = 4

add_result = add(num1, num2)
logging.debug('Add {} & {} to get {}'.format(num1, num2, add_result))

sub_result = subtract(num1, num2)
logging.debug('Subtract {} & {} to get {}'.format(num1, num2, sub_result))

div_result = divide(num1, num2)
logging.debug('Divide {} & {} to get {}'.format(num1, num2, div_result))

mult_result = multiply(num1, num2)
logging.debug('Multiply {} & {} to get {}'.format(num1, num2, mult_result))
