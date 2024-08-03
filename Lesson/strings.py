firstName = "Beatrice"
lastName = "Majang"
# usually both sides of the operator is numbers
# if they are number we can perform addition

# if both sides are string we can perform "string concatenation"
fullName = firstName + " " + lastName
print(fullName)

carPlate = "QTD"
numberPlate = 1996
# however this use case we cannot add thwm because because one is number
# another one is string
# carPlateNumber = carPlate + numberPlate
# I can only concatenate str (not "int") to str
# in this case we cannot convert carPlate to numberPlate
# so let us convert numberPlate to string using str function
carPlateNumber = carPlate + str(numberPlate)
print(carPlateNumber)

# In python, you can multiply string with integer
# when we do this, it will product "times" effect
product = "book"
print(product * 5)
print("=" * 20)

# so far we know strings are enclosed with double quote
# or single quote to differentiate the variable
# we can also use triple double quote or triple single quote
message = "My name is Beatrice. I love Machine learning. I am always..."

# Traditionally how we handle multiline strings
# we handle it using concatenation
# however we still miss the new line characters
# we have to introduce a special character "\n"
# the slash "\" character is also called escape character
# the slash followed by "t" means tab key
# the slash followed by "r" means carriage return
message = "My name is Beatrice\n"
message = message + "I love Machine \tlearning\n"
message = message + "I am al\rways..\n"
print(message)

myfile = "c:\newfolder\table\read.txt"
print(myfile)
# we suppose to tell python to igore the escape sequence
# you can add extra escape sequence
myfile = "c:\\newfolder\\table\\read.txt"
print(myfile)
# however in python we also have special strings called raw strings
myfile = "c:\newfolder\table\read.txt"
print(myfile)

# so far we know strings are enclosed with double quote
# or single quote to differentiate the variable
# we can also use triple double quote or triple single quote
message = """My name is Beatrice. 
I love Machine learning. 
I am always..."""
print(message)

# relationship between string and list
# strings are nothing but list of characters
mygreeting = "Hello world"
print(mygreeting[0])
print(mygreeting[0:6])
print(mygreeting[0::2])
print(mygreeting[0::-1])

# when i started this python class I said all these literals
# are objects
# "Television" is a string literal / string value
# "Television" is also called string object
# objects have functions inside

import sys
product = sys.argv

product = "Television Cloths Vegetables Fruits"
print(product.split())
# this split function takes the literal assigned to the
# variable product and split them or tokenize them into multiple
# words using space as separator since it is going to return
# more than 1 word, it is going to be list of words.
# Functions inside the object is also called "Method".
# From now you must say "print is a function"
# where as "split is a method" 
