# -*- coding: utf-8 -*-
"""
Python code to experiment with Classes. It includs :
Defining : a class, attributes of the class & methods used in the class

Precendance of attributes with then Class structure and instances of the class

"""

# Define a Class structure - the concept of a Class is similar to a blueprint
# Many individual instances may be use the same Class structure ...
# ... but have some individual modifiction/additions to the attributes

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
        """ method to create and return string containing the the employees fullname
            by concatenating the first & last name
        """
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        """Apply a raise to the employees salary
        """
        #Access class variable through the class i.e. Employee (as below)
        self.pay = int(self.pay * self.salary_raise)
        # alternatively access through the instance i.e. Employee.salary_raise
#        self.pay = int(self.pay * Employee.salary_raise)
    # BUT this will use the value specfied in the class for ALL employees
    # and will override the value given in any instance of the class

# Now create two instance variables of the Employee class i.e. 2 employees
# Instance variables contain data that is unique to each instance
emp1 = Employee('John', 'Doe', 20000)
emp2 = Employee('Jane', 'Smith', 30000)
print("Number of employees = {}\n".format(Employee.num_employees))

#To get the fullname, call instance.method() i.e. empl1.fullname
print('Fullname from instance.method() : {}'.format(emp1.fullname()))
# Print off *attribute* data of the instance
print("Pay : {}, E-mail : {}".format(emp1.pay, emp1.email))

#The code below also prints off the fullname
#It calls the Method on the Class but the instance must be added as 'self'
print("Fullname from Class.method() : {}\n".format(Employee.fullname(emp1)))

# It's annual raise time!
# Apply the salary_raise amount and print the raise & new pay
#Notice that some employees get different raise amount
emp1.apply_raise()
print("Emp1 pay after raise of {} = {}\n".format(emp1.salary_raise, emp1.pay))

#Promotion & good raise for emp2!.
#Note change the *instance* attribute salary_raise in emp2
#This will override/take precedance over the Class variable Employee.salary_raise
emp2.salary_raise = 1.1
emp2.apply_raise()
print("Emp2 pay after raise of {} = {}\n".format(emp2.salary_raise, emp2.pay))

#Interesting commands to print the name space of the instance & class
#Note that salary_raise is included in emp2 & the Employee class but not emp1
print("Instance emp1.__dict__ : {}\n".format(emp1.__dict__))
print("Instance emp2.__dict__ : {}\n".format(emp2.__dict__))
print("Class Employee.__dict__ : {}\n".format(Employee.__dict__))
 