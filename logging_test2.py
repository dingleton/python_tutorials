# -*- coding: utf-8 -*-
"""
Sample python code to test/experiment with the logging function
"""

import logging

#Useful link - https://docs.python.org/3/howto/logging-cookbook.html

#Step 1 : Create a logger based on the dunder name attribute
logger = logging.getLogger(__name__)
#Step 2 : set the logging level,
#heirarchy is : NOTSET->DEBUG->INFO->WARNING->ERROR->CRITICAL
logger.setLevel(logging.DEBUG)

#Create the logging formatter - i.e. the format of the log message
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s- : %(message)s')

#Create a file handler to : (a) capture the logging messages,
#(b) set the logging level & (c) set the Log message format.
#Note the logging level is re-defined and will override the 
#logger.setLevel above.
file_handler = logging.FileHandler('logging_test2.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
#
#Create a stream handler to define the messages going to the console
#This uses the same mnessage formatter
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

#Now add both handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    """Add function"""
    return x + y

def subtract(x, y):
    """Subtract function"""
    return x - y

def multiply(x, y):
    """multiply function"""
    return x * y

#add a logger excpetion for a divide by zero error
def divide(x, y):
    """divide function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception("Which fool tried to divide by zero??")
    else:
        return result
    
num1 = 10
num2 = 0    #set to zero to create an error in the divide function

add_result = add(num1, num2)
logger.debug('Add {} & {} to get {}'.format(num1, num2, add_result))

sub_result = subtract(num1, num2)
logger.debug('Subtract {} & {} to get {}'.format(num1, num2, sub_result))

div_result = divide(num1, num2)
logger.debug('Divide {} & {} to get {}'.format(num1, num2, div_result))

mult_result = multiply(num1, num2)
logger.debug('Multiply {} & {} to get {}'.format(num1, num2, mult_result))
