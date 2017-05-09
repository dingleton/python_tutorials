# -*- coding: utf-8 -*-
"""
Program that measure the time taken and memory used by a large number of calls to
both a function & generator.
This shows the generator is (i) faster and (ii) uses much less memory
Code is taken from YouTube tutorial by Corey Schafer
"""

import random
import time
import memory_profiler

#create two lists, one for name and the second
names = ['John', 'Angela', 'Charles', 'Eugenie', 'Hazel', 'Robin']
majors = ['Maths', 'Sport', 'Computing', 'Nuclear Physics', 'Catering',
          'Engineering']

#Print the memory used at the start of the program
print("Memory used at start = {}MB".format(memory_profiler.memory_usage()))

million = 1000000

def people_list(num_people):
    """ loop to create a dictionary
    for the number of iterations stated in function argument
    1. randomly select a name & major subject from, then ..
    2. add them and and the loop variable/id to a dictionary
    """
    result = []
    for i in range(num_people):
        person = {
            'id' : i,
            'name' : random.choice(names),
            'major' : random.choice(majors)
            }
        result.append(person)
    return result

def people_generator(num_people):
    """ loop to create a dictionary
    for the number of iterations stated in generator argument
    1. randomly select a name & major and
    2. add them and and the loop variable/id to a dictionary
    """
    for i in range(num_people):
        person = {
            'id' : i,
            'name' : random.choice(names),
            'major' : random.choice(majors)
            }
    yield person

t1 = time.clock()
people_1 = people_list(million)
t2 = time.clock()
print('\nTime taken by function = {} sec'.format(t2-t1))
print("Memory used after {} function calls = {} MB".
      format(million, memory_profiler.memory_usage()))


t3 = time.clock()
people_2 = people_generator(million)
t4 = time.clock()

print('\nTime taken by generator = {} sec'.format(t4-t3))
print("Memory used after {} generator calls = {} MB".
      format(million, memory_profiler.memory_usage()))
