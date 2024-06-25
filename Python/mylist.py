# there are 4 different types of built in data structure in python

fruits = ["apple", "orange", "mango", "banana", "grapes"]
# fruits is a variable assigned with multiple value(s)
# fruits is also called object, if anything is called as object means it 
# is instance of a class
# John, Peter, Andrew, Matthew are objects, instance of Human Class
# John has eyes(2), nose(1), legs(2) => properties
# John can walk, can run, can eat, can teach, can listen => methods
# fruits object also will have its own properties and methods
print(fruits)

# Indexing and Selection
# Refer to variablesparttwo.py

# modifiable
fruits.append("durian")
# the items gets added as last item
print(fruits)

# insert items inside the existing list
fruits.insert(1, "rambutan")
print(fruits)
fruits.insert(3, "cempedak")
print(fruits)

# update items in the list
fruits[5] = "mangosteen"
print(fruits)

# how to remove an item from the list
fruits.remove("durian")
print(fruits)

# to remove the last item you can use the method pop
fruits.pop()
print(fruits)

# to delete an item by index, we can delete anything from memory permanently
# using the keyword del
greeting = "Good morning"
del greeting
# print(greeting) # NameError
# print([1, 2, 3, 4, 5] + 5) # TypeError
del fruits[3]
print(fruits)

# If you want to clear the list (remove all the items in the list)
fruits.clear()
print(fruits)

# this will delete the entire list
del fruits
# print(fruits)

fruits = ['apple', 'mango', 'orange', 'mango', 'apple', 'banana', 'grapes', 'apple']
print(fruits.index('mango')) # 0, 1

newfruits = fruits[2:] # 0, 1
print(fruits.index("mango") + 1)

# Enumerate is an iterable object
# but print do not know how to iterate the enumerate object
# however we can typecast the enumerate object to a list using list function
print(list(enumerate(fruits)))
# Enumerate returns list of tuple
# Each tuple has 2 items, the first item is the index and the second item is the fruit
for item in enumerate(fruits):
    print(item)

for item in enumerate(fruits):
    #print(item[0])
    #print(item[1])
    if item[1] == "mango":
        print("Mango is in position: ", item[0])

# you may want to know how many apples are there in the list
print("Total number of apples: ", fruits.count("apple"))

# there are other functions which can help us to sort the items in the list
# ascending order from A to Z
fruits.sort()
print(fruits)

# to reverse the list
fruits.reverse()
print(fruits)

for fruit in fruits:
    print(fruit)

# the following is to demonstrate shallow copy
x = [10, 20, 30, 40, 50]
y = x
print(x)
print(y)
x[2] = 35
print(x)
print(y)

# to perform deep copy
x = [10, 20, 30, 40, 50]
y = []
for i in x:
    y.append(i)
print("=" * 40)
print(x)
print(y)
x[2] = 35
print(x)
print(y)

# use copy method instead of use for loop
x = [10, 20, 30, 40, 50]
y = x.copy()
print("=" * 40)
print(x)
print(y)
x[2] = 35
print(x)
print(y)

# fruits is an instance of a list class
# technically the objects are created by calling the class (list)
x = list([15, 25, 35, 45, 55])
print(x)
# however, in oerder to create the list instead of using class they
# let you to use []
x = [12, 22, 32, 42, 52]
print(x)

# to invoke or call the operator we use is () parenthesis (round bracket)
# () is used in expressions
# to call built-in funtion: print() sum() id()
# to create object we call the built-in class: type() int() float() list() 
# to call function inside a module sys.path()
# to call built-in method in a object "Television".split()

def total(numbers):
    result = 0
    numbers[2] = 35
    for number in numbers:
        result = result + number
    return result

x = [10, 20, 30, 40, 50]
print(x)
print(total(x))
print(x)
# the above is the reason why should not send list as arguments
# this is the main reason why python always convert collections to tuple object
# it is understandable now how to convert list to tuple
# you pass the list to the tuple class it will return tuple object
x = tuple(x)
# print(total(x))

# one last feature in list
# list can auto explode
# explode means create 1 variable for every item in the list
fruits = ["apple", "orange", "mango"]
fruit01 = fruits[0]
fruit02 = fruits[1]
fruit03 = fruits[2]

# however in python you no need to explode manually
fruit01, fruit02, fruit03 = fruits
# in other words we are assigning multiple item in the list to multiple variables

