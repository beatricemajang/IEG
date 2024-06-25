# deep copy
fruits = ["apple", "orange", "mango", "banana", "grapes"]
prices = [2.50, 3.29, 1, 8.45]
overseafruits = fruits
# you shouldn't actually do this
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
print(overseafruits)

priceswithsst = []
for price in prices:
    priceswitsst = price + (price * 0.06)
    priceswithsst.append(priceswitsst)
print(priceswithsst)

# using list comprehension
priceswithsst = [price + (price * 0.06) for price in prices]
print(priceswithsst)

# task which we need to do is to find pricewithsst
# you need proce
# now using the above information create a function
def calculateSST(price):
    priceswithsst = price + (price * 0.06)
    return priceswithsst

# this map function takes 2 parameter
# 1st parameter is the function and 2nd paramete is the list
priceswithsst = map(calculateSST, prices)

# what map does?
# inside map there is a loop which pulls out the price from proices
# and pass the price to our function. Our function return the price with sst
# now map append this return value inside a list
# finally once all the prices are iterated the map function returns the list


fahrenheitvalues = [32, 33, 34, 35, 36, 37, 38, 39, 40]
celsiusvalues = []
for fahrenheitvalue in fahrenheitvalues:
    celsiusvalue = (fahrenheitvalue - 32) * 5 / 9
    celsiusvalues.append(celsiusvalue)
print(celsiusvalues)

celsiusvalues = [(fahrenheitvalue - 32) * 5 / 9 for fahrenheitvalue in fahrenheitvalues]
print(celsiusvalues)

# all the three above examples are trying to create a new list
# the number of items in oth list are same
# instead of writting the traditionally for loops
# you can use something called list comprehension

multiplesoftthree = []
for number in range(1, 50): # list of 50 items
    if (number % 3 == 0):
        multiplesoftthree.append(number)
multiplesoftthree = [number for number in range(1, 50) if number % 3 == 0]

# new_list = [expression for number in numbers condition]

numbers = [2, 5, 7, 3, 4, 6, 10, 11, 15, 17, 24, 22]
oddnumber = []
for number in numbers:
    if number % 2 != 0:
        oddnumber.append(number)



# all the abovw two examples are trying to create a new list
# the number of items in the created list is less than or equals to original list
'''
sum = 0
for number in range(1, 11):
    sum = sum + number

mean = 0
for number in range(1, 11):
    mean = mean + number
mean = mean /len(range(1, 11))
'''

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mul = []
for i in num:
    i *= 2
    mul.append(i)
print(mul)

mul = [i * 2 for i in num]
print(mul)

# reduce is not a built in function
# it is inside a module called functools
from functools import reduce

numbers = [1, 2, 3]

def findTotal(oldvalue, currentvalue):
    return oldvalue + currentvalue

print(reduce(findTotal, numbers))
# reduce function takes another funtion as first parameter
# that function suppose to take 2 parameter
# reduce function takes list as second parameter

def reduce(func, numbers):
    sum = 0
    for number in numbers:
        sum = func(sum, number)
    return sum

def factorial(oldvalue, currentvalue):
    return oldvalue * currentvalue

print(reduce(factorial, numbers))




