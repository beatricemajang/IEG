# Methods are nothing but functions inside the class
# Methods take atleast 1 parameter (self)
# This parameter is used by python to pass the instance
class calculator:
    # since this method take self as parameter (instance argument)
    # this method can also be called as instance method
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # since this method also take self as parameter (instance argument)
    # this method can also be called as instance method
    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

mycalculator = calculator(20, 10)
print(mycalculator.add())
print(mycalculator.subtract())

# Why methods take self as a parameter ? Because we want to access the properties
# There is a class which has many methods but no properties
# Which means the methods no need to take self as paramter anymore
# Since there is no property we no need to create Objects
# these type of methods are attached to the class not to the object
# they are called class methods
class Utility:

    def addition(x, y):
        return x + y
    
    def subtraction(x, y):
        return x - y
    
print(Utility.addition(100, 200))

# however this can be easily done just using module in python
# no need to create a class

# There are some use cases where class has properites
# But one or two methods inside class do not require to access the properties
# those methods can be created without self parameter
# and they class methods
class Customer:

    # instance method
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    # class method (because not take self as parameter)
    # usually this class methods are utility functions
    def getFullname(firstname, lastname):
        return firstname + lastname
    
    # instance method
    def __str__(self):
        return Customer.getFullname(self.firstname, self.lastname)
    

myCustomer = Customer("John", "David")
print(myCustomer)