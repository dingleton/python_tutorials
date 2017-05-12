"""

Sample Python code to (i) use property Decorators
(ii) create setters, getters & deleters

"""

#Note - this code is based on create a class that defines data associated with
#an employee. The first & last names are passes into the class and all other data
#is derived from this.

# This is based on a You Tube tutorial by Corey Schafer-
# Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters


class Employee:
    """Define Employee class and add fist & last name to 'self'
    """
    def __init__(self, first, last):
        self.first = first
        self.last = last
    #create an Employee class that accepts two arguments ...
    # ... first (name) and last (name)

    @property
    def email(self):
        """
        Decorated function to return a string containing a Employees e-mail
        """
        return '{}.{}@email.com'.format(self.first, self.last)
    #create a method to generate an e-mail address of format 'first.last@email.com'
    #however we can access this is an attibute and not a method in the main code
    #i.e. variable.email, not variable.email()

    @property
    def fullname(self):
        """ Decorated function to return a string with first & last name
        """
        return '{} {}'.format(self.first, self.last)
    #create a method to generate a fullname of format 'first last'

    @fullname.setter
    def fullname(self, name):   #define a method within the setter
        first, last = name.split(' ')
        self.first = first
        self.last = last
    # create a setter that takes a fullname 'first last' the split this into ..
    # .. the first and last names
    # Note - name of setter = name of property i.e. fullname

    @fullname.deleter
    def fullname(self):
        print('Deleting name!')
        self.first = None
        self.last = None
    #clean up code to delete the name of an employee
    #a print statement is included to show code executes

#create an employee object, an instance (emp_1) of an Employee class
emp_1 = Employee('Barney', 'Rubble')
print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)

# Change emp_1 by setting the 'fullname' attribute
# The @fullname.setter will parse this and set first and last to new values.
# In turn, the e-mail method will set the e-mail to the new value
emp_1.fullname = 'Fred Flintstone'
print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
