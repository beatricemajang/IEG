# so far we have learnt how to assign single value to a single 
# variable. We also learn how to assign multiple values to 
#multiple variables in the same line.
# fruit = "Apple"
# fruit_1, fruit_2 = "Apple", "Orange"

# Now we are going to learn how to assign multiple values
# to a single variable.
# Lets say we want to go for shopping
# We already have list of items to buy in mind
# Lets say we want to but 10 items, doesn't mean we going
# to create 10 variables and assign each item to each variable
# This is where we use a new data structure called "list"
# In other programming language, they call it as "array"
fruits = ["apple", "orange", "mango", "banana", "grapes"]

# indexing and selection
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])

# how many items are there in the list
# there is a built in function len()
print("Number of items we have:", len(fruits))

# how to find the maximun index
print("Maximun index:", len(fruits) - 1)

# does the index has to be positive number?
# not necessary it can even be negative number (only in python)
print(fruits[-1]) # the last item in the list
print(fruits[-2]) # the last but previous item in the list
# This also enable us to retrieve values in a reverse order

# range start_index:end_index
# In python when we refer to range the end_index is not included
print(fruits[1:3])
print(fruits[1:4])

# What if we did not mention the start index
print(fruits[:4])
# since we never mention the start index it will take start index as 0

# What if we did not mention the end index
print(fruits[1:])
# since we never mention the end index it will untill the last time

# In the range we can have third number which represent the step up value
fruits = ["apple", "rambutan", "orange", "durian", "mango", "cempedak", "banana", "mangosteen", "grapes"]
# since we want to include grapes also we use 9 as end index
print(fruits[0:9])
# However, I do not want all the items but only the items in the even positions
print(fruits[0:9:2])
print(fruits[0:9:3]) # this feature is very important for us to take sample
# for example, let's say we have 1 million records
# but we do not want to take all the data and process it
# we want to take sample of 50 items only
# and the selection must be evenly distributed then we can use this step up argument (fruits)

# in the range also you can have negative numbers
print(fruits [-5:-1]) # position -1 has grapes however it is not included
print(fruits [-1:-5]) # -1 > -5 start index is greater than end index result is empty list
# this is because by default step up is 1 -1 +1
print(fruits [-1:-5:-1]) # over here item at -5 is not included
# which means if you want to reverse the entirelist
print(fruits [::-1])