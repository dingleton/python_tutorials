# -*- coding: utf-8 -*-
"""
Python code to experiment with Classes. It includes :
(i) working with subclasses & (ii) inheritance
"""

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

    def __init__(self, first, last, pay):
        #Note. the instance of the class i.e. 'self' ...
        #... is automatically passed as the first parameter
        self.first = first         #first, last, pay etc are attributes of the class
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


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

class Developer(Employee):
    #Developer class inherits from the Employee class
    """
    Define the Develpper class - a subclass of Employee class
    An extra attribute of prog_lang (Programming language) is added
    """
    def __init__(self, first, last, pay, prog_lang):
        #the super().__init__ automatically copies first, last & pay from the
        #Employee patent class
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        #The following line will also work for single inheritance ...
        #... but is not recommended.
        #Employee.__init__(self, first, last, pay)

        #Using the super().__init__() is more maintainable ..
        #..and will work with multiple inheritance

    #Apply a different salary raise amount to the Developer class that ..
    #.. overwrites the the Employee class salary raise amount
    salary_raise = 1.1

class Manager(Employee):
    """ Define the Manager class, a subclass of Employee class
    An class specific attribute are added to define their team
    Class Methods are used to add & remove employees to.from their team
    and print a list of their team
    """
    def __init__(self, first, last, pay, team=None):
        super().__init__(first, last, pay)
        #To avoid passing a mutable list object as a default argument..
        ##.. use the code below
        if team is None:
            print ("Team = None")
            self.team = []
        else:
            self.team = team
            print ("Team != None")

    def add_empl(self, empl):
        """ Method to add an Employee from a managers team
        """
        if empl not in self.team:
            self.team.append(empl)

    def rem_empl(self, empl):
        """ Method to remove an Employee from a managers team
        """
        if empl in self.team:
            self.team.remove(empl)

    def print_employees(self):
        """ Method to print a list of Employees in a manager team
        """
        for empl in self.team:
            print("-->> {}".format(empl.email))

# Now create some instance variables of the Employee class i.e. 2 developers,
# one employees and one manager
# Instance variables contain data that is unique to each instance.
# Although Developer and Manager classes have contain the same attriubutes
# and methods as the parent Employee class, these can also define their
# own methods and attributes that are unique to their class
dev1 = Developer('John', 'Doe', 20000, 'Java')
dev2 = Developer('Peter', 'Perfect', 22000, 'Python')
empl1 = Employee('Lara', 'Croft', 30000)
mgr1 = Manager('Boris', 'Johnson', 50000, [dev1])

# Now perform some print statements to confirm the code fuctions correctly
print(dev1.fullname(), dev1.prog_lang)
print(empl1.fullname(), empl1.pay)

#Use the methods unique to the Manager class
print(mgr1.fullname())
print(mgr1.print_employees())

mgr1.add_empl(dev2)
print(mgr1.print_employees())

mgr1.rem_empl(dev2)
print(mgr1.print_employees())


#Useful Help command to print out info on Developer class.
#Note the Method resolution order in finding the __init__ method ...
#... Developer->Employee->Builtins
#print(help(Developer))

#Useful function isinstance checks if an object is an instance of a class
print("Is object mgr a subclass of Manager? :{}".
      format(isinstance(mgr1, Manager)))
print("Is object mgr a subclass of Employee? :{}".
      format(isinstance(mgr1, Employee)))
print("Is object mgr a subclass of Developer? :{}\n".
      format(isinstance(mgr1, Developer)))

#Useful function issubclass checks if a class is derived from another class
# or is the same class
print("Is Manager a subclass of Manager? :{}".
      format(issubclass(Manager, Manager)))
print("Is Manager a subclass of Employee? :{}".
      format(issubclass(Manager, Employee)))
print("Is Manager a subclass of Developer? :{}".
      format(issubclass(Manager, Developer)))
