# -*- coding: utf-8 -*-
"""
Second module to test __name__ == "__main__"
This module is include in name_main_1 or can be run separarely
"""

print ("At the start of second module")

def module2():
    if __name__ == "__main__":
        print("In second module and __name__ = {}".format(__name__))
    else:
        print("In second module and __name__ = {}".format(__name__))

module2()