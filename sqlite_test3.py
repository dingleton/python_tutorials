# -*- coding: utf-8 -*-
"""
Python code to test/experiment with code to create a sqlite3 database 
"""

import sqlite3 as sql3

def create_table():
    """ Function to create a table in a database
    """
    c.execute("""CREATE TABLE IF NOT EXISTS car_table (
            make TEXT, model TEXT, type TEXT, 
            year INTEGER, mileage INTEGER, price INTEGER)""")

def data_entry_1(car_data):
    """
    Function to enter values into the database table
    """
    with conn:
        c.execute("""INSERT INTO car_table 
                  (make, model, type, year, mileage, price)
                  VALUES (?, ?, ?, ?, ?, ?)""", car_data)
    #This construction of the INSERT statement is more secure and avoids..
    #..potential injection errors from rogue strings
    #Data must be a tuple, even if it only has one value e.g ('xxxx',)
    #Connection object is used as a context manager ...
    #..this automatically commits the data (unless these is an exception)

def data_entry_2(car_data):
    """
    Function to enter values into the database table
    """
    with conn:
        c.execute("""INSERT INTO car_table VALUES
                  (:make, :model, :type, :year, :mileage, :price)""",
                  {'make': car_data[0], 'model' : car_data[1],
                   'type' : car_data[2], 'year' : car_data[3],
                   'mileage' : car_data[4], 'price' : car_data[5]})
    #Alternative construction of the the INSERT statement,
    #data is passed in a dictionary construction
    #Comments on with conn: as above

#Define names of database file & table
sql3_file = 'Magnificent_Motors.db'
car_table = 'cars_for_sale'

#Define & the initial & new stock of cars 
initial_stock = [('Ford', 'Focus', 'Hatchback', 2011, 45900, 4000),
                ('Kia', 'Ceed', 'Estate', 2014, 32000, 8000),
                ('Ford', 'Fiesta', 'Hatchback', 2016, 19750, 6000),
                ('Fiat', '500', 'Saloon', 2013, 37000, 5900),
                ('Skoda', 'Fabia', 'Estate', 2014, 32000, 7200)]
new_car_1 = ('Ford', 'Mondeo', 'Hatchback', 2010, 100000, 3750)
new_car_2 = ('Citroen', 'C2', 'Hatchback', 2015, 10500, 8200)

#Create a connection & cursor
#sqlite3.connect() will create a file if none exists
conn = sql3.connect(sql3_file)
c = conn.cursor()

#Call function to create the table. 
create_table()

#Populate the table with initial stock of cars
for i in range(0, len(initial_stock)):
    data_entry_1(initial_stock[i])

#Add two new cars to the table in the database using the second 
data_entry_2(new_car_1)
data_entry_2(new_car_2)

#Commit the data to the table/database
#Note - this not required since the with conn: ..
#.. command was added to the data_entry_1 & 2 functions
#conn.commit()

c.close()

conn.close()