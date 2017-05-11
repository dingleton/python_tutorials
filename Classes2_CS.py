# -*- coding: utf-8 -*-
"""
Python code to experiment with Classes. It includes :
(i) Defining class methods (ii) using classmethods as alternate constructors
& specific use cases & (iii) static methods
"""

import datetime

class Employee:
    """ Definition of Employee class. It
        a. Create a class attributes of : first & last name, Pay, e-mail
        b. Define class methods to create the Fullname & pay after a salary raise
        c. Define Class variable for (i) Salary raise amount and
            (ii) to count the number of employees
    """

    # Create class variables, these are shared amongst all instances of a Class
    salary_raise = 1.04
    #this will change/be overwritted later for different instances of the class

    num_employees = 0
    #This variable will remain as a class variable.

    def __init__(self, first, last, pay):
        #Note. the instance of the class i.e. 'self' ...
        #... is automatically passed as the first parameter
        self.first = first         #first, last, pay etc are attributes of the class
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        #Increment the number of employees
        Employee.num_employees += 1

        #create methods within the class, don't forget to add 'self'
    def fullname(self):
        """ method to create and return a string containing the the employees
            fullname by concatenating the first & last name
        """
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        """Apply a raise to the employees salary
        """
        #Access class variable through the class i.e. Employee (as below)
        self.pay = int(self.pay * self.salary_raise)

    @classmethod
    #Using a decorator alters the functionality of the method.
    #The *class* is passed as the first argument
    def set_raise_amt(cls, amount):
        """Class method to set the salary_raise attribute
        """
        cls.salary_raise = amount

    @classmethod
    def from_string(cls, emp_str):
        """Method to take a dash '-' separated employee data
        in the format firs-last-pay, separate into it's individual attributes.
        Then populate the class with the attributes and return
        """
        #split the string into it's three variables
        first, last, pay = emp_str.split('-')
        #Now create a *class variable* & return it
        return cls(first, last, pay)

    @staticmethod
    #static methods do *not* automatically pass any data e.g. instance/self or
    # class/cls. They can be thought of a regular functions
    #Typically they have some logical connection with the class and are
    #defined as a static method within the class
    def isworkday(day):
        """Returns True id day is a weekday, False otherwise
        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# Now create two instance variables of the Employee class i.e. 2 employees
# Instance variables contain data that is unique to each instance
emp1 = Employee('John', 'Doe', 20000)
emp2 = Employee('Jane', 'Smith', 30000)

#Run method set_raise_amt. This will operate on the Class and ...
#... overwrites the code that define a the Salary_raise amount in the
#Employee class definition
Employee.set_raise_amt(1.06)

#The alternative code is
#Employee.salary_raise = 1.07

#It is possible to run the class method from the instance...
#... but there is little use for this in practise
#Code is below, not this will change the *class* variable to the given value
#emp1.set_raise_amt(1.01)

print("Employee.salary_raise = {}".format(Employee.salary_raise))
print("emp1 salary_raise ={}".format(emp1.salary_raise))
print("emp2 salary_raise ={}".format(emp2.salary_raise))

#Now use class methods as *alternative constructors*
#Assume formt of info on an employee is split by a dash (-)
# i.e. format first-last-salary
# This needs to be split into individual objects

emp3 = Employee.from_string('Freddy-Mercury-60000')
print("\nemp3, first name = {}, last name= {}, email = {}\n".
      format(emp3.first, emp3.last, emp3.email))

#Now try the static method.
#a. define a date
#b. pass into static method of the class Employee and print true/false
my_date = datetime.date(2017, 5, 10)
print("{} in Mon-Fri? : {}".format(my_date, Employee.isworkday(my_date)))
my_date = datetime.date(2017, 5, 7)
print("{} in Mon-Fri? : {}".format(my_date, Employee.isworkday(my_date)))
