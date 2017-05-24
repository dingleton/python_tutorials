# -*- coding: utf-8 -*-
"""
Python code to test/experiment with sqlite3 commands to :
1. Read table from a database
2. Change or Update an entry
3. Delete a database entry
Note - Database is defined & created by program sqlite_test3.py
"""

import sqlite3 as sql3

def read_and_print_car_table_1():
    """ Function to print all entries in the table 'car_table'
    """
    c.execute("SELECT * FROM car_table")
    for row in c.fetchall():
        print(row)

def read_and_print_car_table_2():
    """ Function to print all entries in the table 'car_table'
    """
    c.execute("SELECT price, year, mileage, make, model, type FROM car_table")
    for row in c.fetchall():
        print(row)

def model_change(car_make, car_model, new_model):
    """ Function to change the entry 'model' from a database element
    """
    with conn:
        c.execute("""UPDATE car_table SET model = :new_model
                  WHERE (make = :make AND model = :model) """,
                  {'new_model':new_model, 'make':car_make, 'model':car_model})

def remove_car(car_make, car_model):
    """ Function to remove a car from the database
    """
    with conn:
        c.execute("""DELETE from car_table
                  WHERE make = :make AND model = :model """,
                  {'make':car_make, 'model':car_model})

#Define database file name & table name
sql3_file = 'Magnificent_Motors.db'
car_table = 'cars_for_sale'

#Create a connection & cursor
conn = sql3.connect(sql3_file)
c = conn.cursor()


#read_the database table & print the results ...but with a different ordering
read_and_print_car_table_2()

#Change the model of one of the cars
print("\n")
model_change('Citroen', 'C2', 'C2 Turbo')
c.execute('SELECT * FROM car_table')
read_and_print_car_table_1()

#Remove a car from the list
print("\n")
remove_car('Ford', 'Mondeo')
c.execute('SELECT * FROM car_table')
read_and_print_car_table_1()

c.close()

conn.close()
