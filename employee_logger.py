# -*- coding: utf-8 -*-
"""
Code to test/experiment with Python logging functions

"""

import logging

#import the module logging_test2.
#Although any code/functions are *not* used below, it will execute and
#create it's own log file. This should contain the module name
#(i.e. logging_test_2) as it's __name__ attribute.
import logging_test2

#Create the logger, use __name__ as the logger name
#Set the loging level to INFO
# Levels are : NOTSET->DEBUG->INFO->WARNING->ERROR->CRITICAL
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#define the format of the log message
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')

#Create a File Handler as a repository of log messages
#& set the log message format.
file_handler = logging.FileHandler('employee_logger.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

#Repeat the above but for the console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


#define Employee class
class Employee:
    """ Create an Employee class to record/create employee data.
    A log message is created each time an instance of the class is created.
    """
    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'
                    .format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@acme_research.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

#Create 3 instances of the Employee class .. and three log messages
empl1 = Employee("Bill", "Gates")
empl2 = Employee("Donald", "Trump")
empl3 = Employee("Alan", "Greenspan")

#finally, close the file handler
file_handler.close()