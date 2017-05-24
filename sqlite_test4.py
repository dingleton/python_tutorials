# -*- coding: utf-8 -*-
"""
Python code to test/experiment with commands to:
a. create a database & table
b. populate/add table entries
c. Interrogate and print entries
"""
import sqlite3 as sql3

def read_car_table():
    c.execute("""SELECT price, year, mileage, make, model, type 
              FROM car_table WHERE price > 5000""")
    for row in c.fetchall():
        print(row)
        
def get_cars_by_make(car_make):
#Note Alternative placeholder construction that uses a dictionary
#to pass parameters
    c.execute("SELECT * FROM car_table WHERE make=:make", {'make': car_make})
    return c.fetchall()

#Define database file name & table name
sql3_file = 'Magnificent_Motors.db'
car_table = 'cars_for_sale'

#Create a connection & cursor
#sqlite3.connect() will create a file if none exists
conn = sql3.connect(sql3_file)
c = conn.cursor()

#1. First of four ways to select cars with 'make'='Ford' &..
#.. print out the entries
print("\n1 of 4 Select & print cars with make = 'Ford'")
c.execute("SELECT * FROM car_table WHERE make = 'Ford'")
[print(row) for row in c.fetchall()]

#2. Second command construction...
#... this uses placeholders & a dictionary to pass arguments.
print("\n2 of 4")
c.execute("SELECT * FROM car_table WHERE make=:make", {'make':'Ford'})
print (c.fetchall())

#3. a function get_cars_by_make  is called to 
print("\n3 of 4")
[print(row) for row in get_cars_by_make('Ford')]

#3. This construction uses a placeholder and passes parameter(s) with a tuple 
print("\n4 of 4")
c.execute("SELECT * FROM car_table WHERE make=?", ('Ford',))
[print(row) for row in c.fetchall()]
print("\n")

#Use fetchone() & fetchmany() methods to fetch
#(i) the first, (ii) the second item then (iii) the following two items 
# from the database
c.execute("SELECT * FROM car_table")
print ("\nFirst entry from fetchone() :{}".format(c.fetchone()))
print ("Second entry from fetchone():{}\n".format(c.fetchone()))

print ("Next two items from fetchmany() {}\n".format(c.fetchmany(2)))

#Finally, select all values from the table & print all contents 
c.execute("SELECT * FROM car_table")
print("\nFinal print of entire database")
[print(row) for row in c.fetchall()]


#Close the cursor and databease connection
c.close()
conn.close()
