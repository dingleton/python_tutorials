# -*- coding: utf-8 -*-
"""
Module to check for __name__ of code modules
Also performs the conditional if __name__ == "__main__"
"""

print ("In first module and about to start importing")

# import code from two different python files,
# note the different ways to import module and their functions
import name_main_2
from name_main_3 import module3

print ("In first module and completed importing")

if __name__ == "__main__":
    print("In first module and __name__ = {}".format(__name__))
else:
    print("In first module and __name__ = {}".format(__name__))

#Call modules 2 & 3. Note the different formats of the call
name_main_2.module2()
module3()