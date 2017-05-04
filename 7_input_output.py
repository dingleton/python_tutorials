# -*- coding: utf-8 -*-
"""
This is code to display variuos output/formatting commands in Python.

It is based on section 7 of the Python tutorial 

"""

#Test the ifference between str, repr and standard print outputs
#Note the repr adds quotes to a string
s = 'Hello Iain'
p = 3.878
t = 7+9j
u = [2.4, 8.5, 9, 2]
v = ('Now ', 2, 5.5, 4 + 1j)

print("\nStr(variable)  = \n", str(s), str(p), str(t), str(u), str(v))
print("\nRepr(variable) = \n", repr(s), repr(p), repr(t), repr(u), repr(v))
print("\nStandard print.format(variable) = \n{} {} {} {} {}\n".format(s, p, t, u, v))

#Note how repr handles \n newline
w = 'the end of the world is neigh\n\n'
print(str(w), repr(w), "\n\n")

#Format a  2-D list of data to be right justified
for x in range(11):
    print("{0:3d} {1:4d} {2:5d}".format(x, x*x, x*x*x))
print("\n")

#Now left justify using the ljust method
for x in range(0, 11):
    print(str(x).ljust(2), str(x*x).ljust(3), str(x*x*x).ljust(4))

print("\n")
#Now center justify using the .center method
for x in range(0, 11):
    print(str(x).center(2), str(x*x).center(3), str(x*x*x).center(4))

#Fill with leading zeros
print("\n")
print('23.0'.zfill(6))      #6 characters inc decimap point
print('-23.0'.zfill(6))     #6 characters inc leading negative & decimal point
print('-23'.zfill(6))       #6 characters inc leading negative
print('23.345657'.zfill(6), '\n')   #6 decimal places


#format a float to a specified number of places, 7 digits + point = 8
num = 6677.1234567
print("\n{0} to 8 places (inc 3 decimal place) is {0:8.3f}\n".format(num))

#Change the order of the format fields
print("{0} plus {1} = 3".format(1, 2))
print("{1} plus {0} = 3".format(1, 2))

#use keywords
print("\nThe winner of {award} award is '{name}'"
      .format(name='Pulp Fiction', award='Best Director'))

#Use both positional & keywords
print("\nMixed arguments, one keyword: {colour} & two positional: {1} & {0}\n"
      .format('Pie', 'Beans', colour='blue'))

#print the contents of a dictionary
tel_list = {'Fred' : 4432, 'James' : 6789, 'Christopher' : 7623}
for name, tel_no in tel_list.items():
    print("{0:11} => {1:4}".format(name, tel_no))

#Now access the dictionary by key. The tel _list is passed as a keyword argument
print('Christopher: {Christopher:d}; Fred: {Fred:d}; James: {James:d}\n'.format(**tel_list))


#Open a text file and display its contents
print("Printing out testfile, one line at a time")
with open('7_testfile.txt', 'r') as f1:
    for line in f1:
        print(line, end='') 

print("\n\nPrinting out testfile :")
print ("(a) 10 characters at a time + (b) Position in file + (c) '%' symbol")

with open('7_testfile.txt', 'r') as f1:
    size_to_read = 10
    f1_contents = f1.read(size_to_read)
    while len(f1_contents) > 0:
        print(f1_contents, f1.tell(), end='%')  #extra % symbol added for clarity 
        f1_contents = f1.read(size_to_read)

#Open the test file and make a copy line by line
with open('7_testfile.txt', 'r') as f1:
    with open('7_testfile2.txt', 'w') as f2:
        for line in f1:
            f2.write(line)

#copy a jpg image file by opening as binary and copying in 2k chunks of data
with open('7_window_repair.jpg', 'rb') as f3:
    with open('7_window_repair_copy.jpg', 'wb') as f4:
        chunk_size = 2048
        data_chunk = f3.read(chunk_size)
        while len(data_chunk) > 0:
            f4.write(data_chunk)
            data_chunk = f3.read(chunk_size)
        
#Use .tell & .seek methods
f5 = open('7_testfile.txt', 'r')
chars_to_read = 8
position = f5.tell()
print("\n\nCurrent file position = {} & {} characters of file data is = '{}'"
      .format(position, chars_to_read, f5.read(chars_to_read)))
position = f5.seek(10, 0)     #Move  position to 10 character into filer
print("\n\nCurrent file position = {} & {} characters of file data = '{}'"
      .format(position, chars_to_read, f5.read(chars_to_read)))
# *** note - I can't get the seek method to work with a second parameter = 1, or 2 
f5.close()
