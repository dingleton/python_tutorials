
# python_tutorials

# This contains a number of python programs written to test the commands given in Python tutorials
# Their output is typically print statments showing the effect of Python commands. In come cases files are copied and log files created. 
# These were tested with Python 3.6 running Windows 10 environment and using teh anaconda environment.
# They are published simply to show my level of competance/learning of the Python programming language
# Tutorials based on those given on the Python Website https://docs.python.org/3/tutorial/ and You Tube content by Corey Schafer https://www.youtube.com/user/schafer5

Python programs to experiment/test the commands in chapters 5, 7 & 8 of the online tutorial

File : 5 Data structures.py
Code to test/experiment with the data structures defined in chapter 5 of the online python tutorial

File : 7_input_output.py + 2 files accessed by this code (7_testfile.txt 7_window_repair.jpg)
These test the Input Output commands in chapter 7 of the online Python tutorial https://docs.python.org/3/tutorial/inputoutput.html
This creates a copy of the jpg file 7_window_repair_copy.jpg.

Files : 8_modules.py & fib_mod.py - this tests the import module function as define in chapter 8 of the online python tutorial.
It imports fib_mod.py which prints and returns the fibonnaci series of numbers.


Below is a list of the programs used to experiment/test with other Python command/modules etc. These were taken from the You Tube tutorials on Python by Corey Schafer https://www.youtube.com/user/schafer5

Datetime module
date_time_tutorial.py
This experiments with various datetime function in naive and non-naive formats.

Decorators
File : property_decorators_CS.py 
This tests the Python @decorator when used with functions. It also creates: setters, getters & deleters

Numpy
File : numpy_arrays.py
Code to test/experiment with the numpy moduke. 

__name__ & __main__
name_main_1.py + _2.py & _3.py. 
These test for the value of __name__ when the code run as the main program or included in a module. Name_main_1.py should be run as a program which imports name_main_2.py & name_main_3.py. The latter two can be run as (main) programs individually. 

Generators
Files : generators1_CS.py & generators2_CS.py.
These define and run Python generarators alongside the equivalent code that uses function calls to get the same result

Classes
Files : classes_1CS.py, classes2_CS.py. classes3_CS.py
These programs have code to define/experiement with Classes include : defining class methods, class attibutes, using classes as alternate constructors, subclasses & inheritance.

Logging
a. File : logging_test1.py.
Code to test/experiment with the python logging functions. This creates a logfile logging_test1.log
By manually setting the variable num2 in line 52 to zero, a divide by zero error message can be generated
b. Files : logging_test2.py & employee_logger.py.
These files uses more advanced logging functions and generate log files logging_test2.log & employee_logger.log. 
logging_test2.py is imported into employee_logger.py. 

When employee_logger.py is run, the imported file logging_test2 will generate an error which is recorded in logging_test2.log & send to the console. Employee_logger creates it's own log file employeer_logger.txt.
Program logging_test2.py can also be run standalone.
Note the format of messages sent to the console & logging files are different.

Sqlite3 database
The following 3 files create, interrogate & modify a sqlite3 database.
a. sqlite_test3.py creates a database/table. This must be run first and will create the file "Magnificent_Motors.db"
b. sqlite_test4.py interrogates the database
c. sqlite_test5.py modifies & deletes some values
