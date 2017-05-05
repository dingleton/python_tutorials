# -*- coding: utf-8 -*-
"""
    Based on Python Tutorial 5 - code to test/experiemnt with Data structures & List comprehensions
    Tested on Python 3.6
""" 

#create a list and count the number of elements
countries = ['uk', 'usa', 'zanzibar', 'uganda', 'argentina']
print ("\nNumber of countries/len(countries) = {}".format(len(countries)))

#now sort in reverse alphabetical order.
countries.sort(reverse=True)
print ("\nSorted in reverse alphabetical order = {}".format(countries))

#add two more countries to teh end of the list and print out
countries.append('brazil')
countries.insert(len(countries), 'canada')
print("Appended list = {}".format(countries))

#now sort in aplhabetical order & pop/remove the last member
countries.sort()
countries.pop()
print ("\nAlphabetically sorted and 'popped' list = {}".format(countries))

#Add a list containing two more countries and remove one from mid way through the list
countries.extend(['netherlands', 'france'])
countries.remove('canada')
print ("Extended list with usa removed = {}".format(countries))

#create a list/stack and append two entries 
stack = [8, 9, 10]
stack.append(11)
stack.append(12)
print("\nappended stack = {}".format(stack))

#now pop/remove the last entry from teh stack
stack.pop()
print("\npopped stack = {}".format(stack))


# Use deque to manage queues - First In First out is shown below
from collections import deque

queue = deque(['abbey', 'brenda', 'christine'])
queue.append('davina')

print ("\nQueue = {}".format(queue))
queue.popleft()
print ("Queue after popleft = {}".format(queue))


#List Comprehensions - concise way to create a list

squares = [x**2 for x in range (1,11)]
print ("\nSquares 1 to 10 = {}".format(squares))

even_tuples = [(x, x**2) for x in range (2, 11, 2)]
print ("\nTuples of even numbers & **2 in range 2 to 10 = {}".format(even_tuples))

#Taken from Python tutorial & adapted the if statement that prevents certain combinations
tuple_list = [(x, y) for x in [ 1, 2, 3] for y in [1, 4, 9] if y != 2*x]
print ("\nTuple list = {}".format(tuple_list))


#This is a very artifical example where the list comprehension calls a function 
#which creates a list of lists of prime numbers 
def prime_numbers(max):
    primes = []
    for n in range (2,max):
        for m in range(2,n):
            if n % m == 0:
                break       # exits **for** loop and not if conditional
        else:
            primes.append(n)
    
    return primes

#list comprehension to create lists of lists of prime numbers
list_of_list_of_primes = [prime_numbers(x) for x in range(3,10)]

print("\nPrime numbers <=20 = {}".format(list_of_list_of_primes))


#Section 5.1.4 Nested List comparisons
#Copied from teh tutorial to try and get my head around this.
matrix = [ 
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18]
        ]
#now transpose the rows and columns
transposed = [[row[i] for row in matrix] for i in range(6)]

print ("\nTransposed matrix by method 1 = \n{}".format(transposed))

#second attempt to do the same thing
transposed = []
for i in range (6):
    transposed.append([row[i] for row in matrix])
print ("\nTransposed matrix by method 2 = \n{}".format(transposed))  

#third attempt to do the same thing
#in this case a transposed row is created and then appended to the new array in one operation.
transposed = []
for i in range (6):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print ("\ntransposed matrix method 3 = \n{}".format(transposed))

#final, a much easier method using the zip function
print ("\nFinal method to transpose using zip function = {}".format(list(zip(*matrix))))

#5.3 Tuples - created by listing values separated by commas

tuple_1 = 3.14 , 66, 'good day', 4 + 7j, [3, 4, 5]

a, b, c, d, e = tuple_1
print ("\na = {}, b = {}, c = {}, d= {}, e = {}".format(a, b, c, d, e))

#Tuples are immutable but can contain mutable opjects inc lists
tuple_1[4][2] = -10
print ("\na = {}, b = {}, c = {}, d= {}, e = {}".format(a, b, c, d, e))


#5.4 Sets

set_1 = { 'a', 'c', 'e', 'd', 'v'}
set_2 = { 'a', 'c', 'm', 'e'}

print ("\nset_1 = {}\nset_2 = {}".format(set_1, set_2))

print ("\nset_1 - set_2 = {}".format(set_1 - set_2))

print ("set_1 or set_2 = {}".format(set_1 | set_2))

print ("set_1 and set_2 = {}".format(set_1 & set_2))

print ("set_1 ^ set_2 = {}".format(set_1 ^ set_2))

set_3 = {x for x in "abcdefgh" if x not in "abc"}
set_4 = {x for x in set_1 if x not in set_2}

print ("\nList comprehension results with sets :\n{}, \n{}".format(set_3, set_4))

#5.5 Dictionaries
emer_phone = { 'Doctor' : 2345441, 'Dentist' : 2345699, 'Plumber' : 3345643 }

#Print the endire dictionary
print("\nEmergengy Phone numbers = {}".format(emer_phone))

print ("\nDoctors phone number is {}".format(emer_phone['Doctor']))

#add one entry (Glazier), amend the Dentist's phone number & delete the Plumbers details
emer_phone['Glazier'] = 1234321
emer_phone['Dentist'] = 2345677
del emer_phone['Plumber']
print("\nEmergengy Phone numbers (revised) = {}\n".format(emer_phone))


#5.6 Looping techniques

for a, b in emer_phone.items():
    print ("Key = {} \tTel no = {}".format(a, b))

print("\n")
for a, b in enumerate(emer_phone.items()):
    print ("Index = {} \tRest = {}".format(a, b))
    
#zip two lists and loop over simultaneously
animal = ['dog', 'cat', 'hamster', 'rat']
name = ['rover', 'tiddles', 'hamish', 'roland']
print("\n")
for a, n in zip(animal, name):
    print ("My name is {1} and I'm a {0}.".format(a, n))
print ("\n")

#Loop through forward & reversed range
start, stop, step = -1, 10, 3
for i, j in zip(range (start, stop, step), reversed(range (start, stop, step))):
    print ("Forward loop value {0}, \tReversed loop value {1}".format(i, j))
print("\n")  

#sort the list is alphabetical order
breakfast = ['muslei', 'cornflakes', 'toast & jam', 'poridge', 'wheatabix']
for i,j in zip(breakfast, sorted(breakfast)):
    print ("{0}, \t{1}".format(i, j))


import math

raw_data = [3.8, 67.3, 4, 5, float('NaN')]
new_data =[]
print("\n")
for i in raw_data:
    if not math.isnan(i):
        new_data.append(i)
print ("New filtered list = {}".format(new_data))