# -*- coding: utf-8 -*-
"""
Third module to test __name__ == "__main__"
This is included/called by name_main_1 or can be run independantly
"""

print ("At the start of third module")

def module3():
    if __name__ == "__main__":
        print("In third module and __name__ = {}".format(__name__))
    else:
        print("In third module and __name__ = {}".format(__name__))

module3()