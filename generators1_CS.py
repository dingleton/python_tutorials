# -*- coding: utf-8 -*-
"""

Generators - sample code to test Python Generators
Taken from Corey Schafers You Tube Tutorial on Python Generators

"""

def square_numbers_1(nums):
    """ function to accept a list of numbers and 
    return a list of the square of each number
    """
    result = []
    for i in nums:
        result.append(i*i)
    return result

def square_numbers_2(nums):
    """A Generator to accept a list of numbers and
    return a list of the square of each number
    """
    for i in nums:
        yield(i*i)

#Create and initialise a small list (my_nums_0). 
#Then generate a new list containing the squares of these numbers.
#This is done three times:
#1. fcalling function square_numbers_1 - this returns a list 
#2. calling a generator square_numbers2, this is then converted to a list
#3. finally a list comprehension is used (for more practise in list comprehensions!)
my_nums_0 = [1, 2, 3, 4, 5]
my_nums_1 = square_numbers_1(my_nums_0)
my_nums_2 = list(square_numbers_2(my_nums_0))
my_nums_3 = [x*x for x in range(min(my_nums_0),max(my_nums_0)+1)]

print(my_nums_1)
print(my_nums_2)
print(my_nums_3)

#now assign the gerator function to a variable
my_nums_4 = square_numbers_2(my_nums_0)
#Print the variable i.e. the address of the **unexecuted** generator
#Next print each value by executing the generator to produce the next result
print("\nmy_nums_4 = {}".format(my_nums_4))
for j in range (0,5):
    print(next(my_nums_4))
