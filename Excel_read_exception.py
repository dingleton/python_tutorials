# -*- coding: utf-8 -*-
"""
Python program to
a. Test some of the commands in xlrd module to read an excel file
b. Use the "try, exception, else" construction
c. Validate the format of data in the excel file by
  (i) checking the type of data
  (ii) checking if the data is within acceptable ranges

The program
(i) reads an excel file "car_stock.xlsx"
(ii) checks the validity of each cell
(iii) store the data in a list and
(iv) prints off the contents of a list

This written/tested in Python 3.6
"""

import datetime
import xlrd

def print_car_data(make, model, year, price, date):
    """ Function to take a list of car data and print this out in a
    formatted line of text
    """
    print("{} {} {}  £{}  Date: {:%d-%m-%Y}"
          .format(make.rjust(12), model.rjust(10), repr(int(year)).rjust(6),\
                    repr(int(price)).rjust(6), date))

source_file = "car_stock.xlsx"

#Open the excel file, xlrd.open_workbook returns an instance of the "Book" class
try:
    workbook = xlrd.open_workbook(source_file)
except xlrd.XLRDError as e1:
    print(e1)
    print("Error : XRLDError - File {} could not be found or opened, please check & try again"
          .format(source_file))
except Exception as e2:
    #Anaconda static code analysis generates a warning "Catching too general exception"
    #However - the xlrd.XLRDError exception above does NOT catch an error in the file name
    print(e2)
    print("Error : Exception - File {} could not be found or opened, please check & try again"
          .format(source_file))
else:
    #File has been opened successfully
    #a. read the excel file containing data of a car dealers stock of cars then
    #b. put/append data in separate arrays of: make, model, Year, Price & Date aquired
    sheet = workbook.sheet_by_index(0)   #Read the first worksheet
    headers = []
    car_data = []
    excel_file_problem = False
    earliest_year = 1980
    latest_year = 2017
    min_price = 1
    max_price = 100000

    #Code below reads and store the text in each column headers in row 1
    #Other that storing the list of header in a list,...
    #...this info is NOT used in the code that read and displays the excel data
    #A future code extension could be to check the headers than automatically
    #.. read/check the data in each column according to type of data/header..
    for col in range(sheet.ncols):
        headers.append(sheet.cell_value(0, col))

    #1. Read all the car stock data from the row 2 onwards,
    #2. Checks the data is (i)the correct type (ii) within certain ranges
    #3. Add the list of data on a single car to a master list
    for row in range(1, sheet.nrows):
        temp_list = []
        #Car make must be alphanumeric characters only, spaces are allowed
        make_excel = sheet.cell_value(row, 0)
        if isinstance(make_excel, str) and (make_excel.replace(" ", "").isalnum()):
            temp_list.append(make_excel)
        else:
            temp_list.append('**' + str(make_excel) + '**')
            excel_file_problem = True

        #Car model can be alphanumeric characters & spaces only
        model_excel = sheet.cell_value(row, 1)
        if isinstance(model_excel, (float or int)):
            #If car model consists of number only, this line is exectuted
            temp_list.append(str(int(model_excel)))
        elif isinstance(model_excel, str) and (model_excel.replace(" ", "").isalnum()):
            #if car model is a string of alphanumeric characters and spaces
            temp_list.append(model_excel)
        else:
            #Error condition - text with "**" before and after data is added
            temp_list.append('**' + str(model_excel) + '**')
            excel_file_problem = True

        #Year must be of type float or integer and must be within a range of years
        # if not, the entry is incorrect and zero value is inserted to the list
        year_excel = sheet.cell_value(row, 2)
        if isinstance((year_excel), (float or int)) and \
        ((year_excel >= earliest_year) and (year_excel <= latest_year)):
            temp_list.append(year_excel)
        else:
            temp_list.append(0.0)
            excel_file_problem = True

        #Price must be contain numeric characters only & be in a valid range
        #The price must be of type float or integer and must be within a range
        # otherwise the entry is incorrect and a zero value is added.
        price_excel = sheet.cell_value(row, 3)
        if isinstance(price_excel, (float or int)) and \
        ((price_excel >= min_price) and (price_excel <= max_price)):
            temp_list.append(price_excel)
        else:
            temp_list.append(0)
            excel_file_problem = True

        #for the date, first read this in excel format
        error_date = (1900, 1, 1, 0, 0)
        date_excel = sheet.cell_value(row, 4)
        if isinstance(date_excel, float):
            #As the Excel format of the date is a float, first check data type
            #In case of a error, insert 01-01-1900 as the date
            try:
                time_tuple = xlrd.xldate_as_tuple(date_excel, datemode=0)
            except xlrd.XLDateError as e3:
                #The exception covers 4 specific errors forxldate_as_tuple
                #See http://www.lexicon.net/sjmachin/xlrd.html
                print(e3)
                temp_list.append(datetime.datetime(*error_date))
                excel_file_problem = True
            else:
                temp_list.append(datetime.datetime(*time_tuple))
        else:
            temp_list.append(datetime.datetime(*error_date))
            excel_file_problem = True

        #Add the list of data on one car to the master list
        car_data.append(temp_list)


    if excel_file_problem:
        print("Invalid data entries in source file '{}'\
               \nErrors can be identifed in the table below\
               \n  String data will be in format **<cell data>**,\
               \n  Numbers will be 0 or 0.0\
               \n  Dates will be set to 01-Jan-1900\
               \nPlease check & correct the excel file and try again\n".format(source_file))

#print out the data shored in the list : car_data[]
    for i in range(sheet.nrows-1):
        print_car_data(*car_data[i])
