# -*- coding: utf-8 -*-
"""
Sample Python code to test some of the numpy functions & methods
"""

import numpy as np

#Create 2 arrays, set their size, indice values, dimensions & data type. 
#them print info on their sizes etc. 
a1 = np.arange(16, dtype=np.int8).reshape(2,8)
print("shape of 'a1' = {}".format(a1.shape))
print("size of 'a1' = {}".format(a1.size))
print("ndim/number of dimensions of 'a1' = {}".format(a1.ndim))
print("dtype/datatype of 'a1' = {}".format(a1.dtype))
print("itemsize of 'a1' = {}".format(a1.itemsize))
print("data of 'a1' = {}".format(a1.data))
print("sum of axis 0 'a1' = {}".format(a1.sum(axis=0)))
print("sum of axis 1 'a1' = {}".format(a1.sum(axis=1)))
print("array 'a1' = \n{}\n".format(a1))

a2 = np.arange(120).reshape(5,4,3,2)

print("shape of 'a2' = {}".format(a2.shape))
print("size of 'a2' = {}".format(a2.size))
print("ndim of 'a2' = {}".format(a2.ndim))
print("dtype of 'a2' = {}".format(a2.dtype))
print("itemsize of 'a2' = {}".format(a2.itemsize))
print("data of 'a2' = {}".format(a2.data))
print("array 'a2' = \n{}\n".format(a2))

#create an array with mixed integer & floats
b = np.array([1, 2.2, 3.2])
print("array 'b' = {}\n".format(b))

#create an array of complex numbers
c = np.array([[1.1,2.5], [3,4.999]], dtype = complex)
print("array 'c' with complex numbers = {}\n".format(c))

#create an array of 1's
d = np.ones([2,3,4], dtype = np.int8)
print("array 'd' of ones= {}\n\n".format(d))

#Define & initilise soem arrays then take perform & print dot products
e = np.array([[1, 2], [3, 4]])
f = np.array ([[5, 6], [7, 8]])
print ("Dot product 1 = {}\n".format(np.dot(e, f)))
print ("Dot product 2 = {}\n".format(e.dot(f)))

#Create 2x3 arrays of random numbers.
#Also create a 2 x 3 array of 1's and multiple each element by 3.
g = np.random.random((2, 3))
print("array 'g' of random = {}\n".format(g))
h = np.ones((2,3), dtype = float)
h *= 3
print("array 'h' of 3*ones = {}\n".format(h))

#Create an 1D array of 1s & linespace (0, pi) and add them together. 
i = np.ones(3, dtype = np.int32)
j = np.linspace(0, np.pi, 3)
k = i +j
print ("array k of ones + linspace from 0 to pi = {}\n".format(k))


#Create an array using numpy/fromfunction
#This define a function & uses it to initialise each entry
# accordinf to teh formula 10 x row co-ordinate + column co-ordinate
def arr_funct(x, y):
    return 10*x + y
#create a 5 X 4 array of integers, initilsie each value using arr_funct() 
k2 = np.fromfunction(arr_funct, (5,4), dtype = int)

print("array k2 with values derived by arr_funct & cell co-ordinates = \n{}\n"
      .format(k2))

l = np.array([[[0,1,2],
              [10,11,12]],
    [[100,101,102],
     [110,111,112]]])

print ("l equals\n{} \n shape = {}\n".format(l, l.shape))

# (i) create a 3 x 4 array,
# (ii) assign with random values
# (iii) multiply each by 10 and
# (iv) take the floor value (iu.e. round to a whole number
#   in the direction of negative ibnfinity)
m = np.floor(10*np.random.random((3,4)))
print ("Array m = \n{}\nShape = {}\n".format(m, m.shape))

#now flatten the array above "ravel"
print ("Flattened array m = {}\n".format(m.ravel()))

#Create 2 of 2 x 2 arrays with random numbers then stack them
o = np.floor(10 * np.random.random((2,2)))
p = np.floor(10 * np.random.random((2,2)))
print ("Array o = \n{}\n\nArray p =\n{}\n".format(o, p))

print ("Vertical stack =\n{}\n".format(np.vstack((o,p))))
print ("Horizontal stack =\n{}\n".format(np.hstack((o,p))))
print ("Column stack =\n{}\n".format(np.column_stack((o,p))))


#Test to assign two variables (q & r) to the same object and 
#confirm they have the same address
#Also confirm when this object is passed into a function
#it retauins the same address
def f2(x):
    print ("ID of parameter 'x' passed into function is {}\n".format(id(x)))

q = np.arange(12)
r = q
print ("ID of q and r is {} & {}".format(id(q), id(r)))

f2(q)
f2(r)


