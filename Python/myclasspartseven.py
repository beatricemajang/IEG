# Multiple inheritance
class Card:
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Card Class")

class AtmCard(Card):
    def __init__(self):
        pass
    # def doSomething(self):
        # print("Inside AtmCard Class")

class CreditCard(Card):
    def __init__(self):
        pass
    # def doSomething(self):
        # print("Inside CreditCard Class")

class DebitCard(Card):
    def __init__(self):
        pass
    # def doSomething(self):
        # print("Inside DebitCard Class")

class BankCard(AtmCard, CreditCard, DebitCard):
    def __init__(self):
        pass
    def doSomething(self):
        # print("Inside BankCard Class")
        super().doSomething()

# we have created 5 classess
# and in all 5 classes we have doSomething method
# and it is implemeneted (got code inside which is "print")

# Let us create instance of the last card
bankCard = BankCard()
bankCard.doSomething()
# you will see "Inside BankCard Class"

# now remove the print statement from bankcard.dosomething
# and call the super().dosomething
# this time you will see "Inside AtmCard Class" (which is the first inherited class)

# now comment the dosomething method which is inside the AtmCard Class
# this time you will see "Inside CreditCard Class"

# now comment the dosomething method which is inside the CreditCard Class
# this time you will see "Inside DebitCard Class"

# now comment the dosomething method which is inside the DebitCard Class
# this time you will see "Inside Card Class"

# Basically what we understand here is 
# python scan from left to right and identify the base classes 
# and call the methods accordingly
# This process is called Method Resolution Order (MRO)
print(BankCard.__mro__)

# <class '__main__.BankCard'>
# <class '__main__.AtmCard'>
# <class '__main__.CreditCard'>
# <class '__main__.DebitCard'>
# <class '__main__.Card'>
# <class 'object'>

# BIGGEST CONCLUSION: 
# Every class we create in python is inherited from a class called object
# class object:
#   def __init__():
#       pass
#   def __str__():
#       return memory address

# class Student(object):
class Student():
    pass
    # def __str__(self):
        # return "Student"

class Alumni(Student):
    pass
    # def __str__(self):
        # return "Alumni"

alumni = Alumni()
print(alumni)

# Hope you guys still remember this
# Iterator object like enumerator, range, map, filter do not override
# the method __str__
# However those classes are inherited from the default python class
# called object which has the method __str__ which 
# returns the address location of the object
# Finally that gets printed using the print function
class object:
    def __str__(self):
        return "address"

class range(object):
    pass

myrange = range()
print(myrange)

# What if i dont want my class to inherit from the base class called object
# Definetly you don't want to do this because
# you will loose all the default feature of a class
class myclass:
    pass

# myclass().will list more methods. 
# now we understand those methods are coming the base class called object

# No I insist I dont want my class to be inherited
class noObjectClass():
    pass

test = noObjectClass()
print(test)
