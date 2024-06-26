# deep copy
fruits = ["apple", "orange", "mango", "banana", "grapes"]
prices = [1.60, 1.20, 2.20, 4.80, 6.20]

# for loop with some statement
for fruit in fruits:
    print(fruit)

# overseafruits = fruits # you shouldn't actually do this
# overseafruits = fruits.copy()

overseafruits = []
# for loop with list
for fruit in fruits:
    overseafruits.append(fruit)
print(overseafruits)

# using list comprehension
overseafruits = [fruit for fruit in fruits]
print(overseafruits)

# using tuple comprehension
overseafruits = (fruit for fruit in fruits)
print(tuple(overseafruits))

priceswithsst = []
for price in prices:
    pricewithsst = price + (price * 0.06)
    priceswithsst.append(pricewithsst)
print(priceswithsst)

# using list comprehension
priceswithsst = [price + (price * 0.06) for price in prices]
print(priceswithsst)

# using map class
# task which we need to do is find pricewithsst
# you need price
# now using the above information create a function
def calculateSST(price):
    pricewithsst = price + (price * 0.06)
    return pricewithsst

# this map function takes 2 parameters
# 1st parameter is the function and second parameter is the list
priceswithsst = map(calculateSST, prices)
print(list(priceswithsst))

# what map does ?
# Inside map there is a for loop which pulls out the price from prices
# and pass the price to our function. Our function return the price with sst.
# Now map append this return value inside a list
# finally once all the prices are iterated the map function returns the list
# def map(func, values):
#    result = []
#    for value in values:
#        result.append(func(value))
#    return result

fahrenheitvalues = [32, 33, 34, 35, 36, 37, 38, 39, 40]
celsiusvalues = []
for fahrenheitvalue in fahrenheitvalues:
    celsiusvalue = (fahrenheitvalue - 32) * 5/9
    celsiusvalues.append(celsiusvalue)
print(celsiusvalues)

# using list comprehension
celsiusvalues = [(fahrenheitvalue - 32) * 5/9 for fahrenheitvalue in fahrenheitvalues]
print(celsiusvalues)

# using map class
def fahrenheitToCelsius(fahrenheitvalue):
    return (fahrenheitvalue - 32) * 5/9
celsiusvalues = map(fahrenheitToCelsius, fahrenheitvalues)
print(list(celsiusvalues))

# in all the above three examples we are trying to create a new list
# the number of items in both list are same
# Instead of writing the traditionaly for loops 
# you can use something called list comprehension or map class

multiplesofthree = []
for number in range(1, 50): # list of 50 items
    if (number % 3 == 0):
        multiplesofthree.append(number)
print(multiplesofthree)

# using list comprehension
multiplesofthree = [number for number in range(1, 50) if (number % 3 == 0)]
print(multiplesofthree)

# using filter class
def findMultiplesOfThree(number):
    return True if (number % 3 == 0) else False
        
multiplesofthree = filter(findMultiplesOfThree, range(1, 50))
print(list(multiplesofthree))

numbers = [2, 5, 7, 3, 4, 6, 10, 11, 15, 17, 24, 22]
oddnumbers = []
for number in numbers:
    if (number % 2 != 0):
        oddnumbers.append(number)
print(oddnumbers)

# using list comprehension
oddnumbers = [number for number in numbers if (number % 2 != 0)]
print(oddnumbers)

# using filter class
def isOddNumber(number):
    return True if (number % 2 != 0) else False

oddnumbers = filter(isOddNumber, numbers)
print(list(oddnumbers))

# all the above two examples are trying to create a new list
# the number of items in the created list is less than or equals to original list
# Instead of writing the traditionaly for loops 
# you can use something called list comprehension or filter class

sum = 0
for number in range(1, 11):
    sum = sum + number
print("Sum:", sum)

mean = 0
for number in range(1, 11):
    mean = mean + number
mean = mean / len(range(1, 11))
print("Mean:", mean)

# in the above 2 examples we are trying to reduce the list to a single value


# reduce is not a built in function
# it is inside a module called functools
from functools import reduce

numbers = [1, 2, 3]

def findTotal(oldvalue, currentvalue):
    return oldvalue + currentvalue

print(reduce(findTotal, numbers))

# reduce function takes another fuction as frist parameter
# that function suppose to take 2 parameter
# reduce function takes list as second parameter
"""
def reduce(func, numbers):
    sum = 0 
    # however the original reduce function is smart 
    # it will initialize the sum variable with 1 if you use multiplication
    for number in numbers:
        sum = func(sum, number)
    return sum
"""

def factorial(oldvalue, currenvalue):
    return oldvalue * currenvalue

print(reduce(factorial, numbers))

# now we are initializing the sum variable with 5
print(reduce(factorial, numbers, 5))