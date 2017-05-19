# -*- coding: utf-8 -*-
"""
Sample python code to test/experiment with the logging function
"""

import logging

#Useful link - https://docs.python.org/3/howto/logging-cookbook.html

#Step 1 : Create/Instantiate a logger object based on the dunder name attribute
#It returns a reference to a logger instance with the specified name
# or root if not.
#The name could be a period-separated hierarchical value, e.g. foo.bar.baz
logger = logging.getLogger(__name__)

#Step 2 : set the logging level,
#heirarchy is : NOTSET->DEBUG->INFO->WARNING(default)->ERROR->CRITICAL
logger.setLevel(logging.DEBUG)

#Step 3 Create the logging formatter - i.e. the final order, structure, 
#and contents of the log message.
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s- : %(message)s')

#Step 4 - Create a file handler to :
#(a) sending the logging messages to the specified destination file 
#(b) Optionally, set the logging level & override logger.setLevel above
#(c) Set the Log message format.
file_handler = logging.FileHandler('logging_test2.log', mode='a')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

#Step 5 Create a stream handler to define the messages going to the console
#This uses the same message formatter
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

#Now add both handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

#note Logger.removeHandler() will remove the handler


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
        #Logger.exception() creates a log message similar to Logger.error()..
        #..and dumps a stack trace. To be called only from an exception handler.
    else:
        return result
    
num1 = 10
num2 = 0    #set to zero to create an error in the divide function

add_result = add(num1, num2)
#Create a logger dubug message
#Other commands include logger.info(), logger.debug(), logger.warning(), ..
#.. logger.error(), logger.critical(), logger.exception()
logger.debug('Add {} & {} to get {}'.format(num1, num2, add_result))

sub_result = subtract(num1, num2)
logger.debug('Subtract {} & {} to get {}'.format(num1, num2, sub_result))

div_result = divide(num1, num2)
logger.debug('Divide {} & {} to get {}'.format(num1, num2, div_result))

mult_result = multiply(num1, num2)
logger.debug('Multiply {} & {} to get {}'.format(num1, num2, mult_result))

file_handler.close()
