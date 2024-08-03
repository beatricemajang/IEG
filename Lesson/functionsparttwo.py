# Whenever we say function immediately we think about 
# 2 things 1) parameter 2) return
# We already know how to pass function as an argument
# we are going to see how to return a function
def authenticate(username, password): # Parent
    def simpleInterest(principle, period, rate): # Child
        def something(): # Grand Child
            pass
        something()
        return (principle * period * rate) / 100
    if (username == "admin" and password == "pwd123"):
        # now we know function can have inner function
        # inner function can be called from the outer function
        # how ever you cannot call the inner function
        # from the main context
        # print("Interest Amount:", simpleInterest(1000, 1, 6))
        return simpleInterest # returning address location where simpleInterest function is

# simpleInterest()
# from main context you cannot call the function (inner function) which is 
# inside another function (outer function)
# however we still can call that function (inner function), if the outer
# function returns the inner function
func = authenticate("admin", "pwd123")
print("Interest amount:", func(1000, 1, 6))

# why inner function
# sometimes the authenticate function itself will get bloated
# and you may come across there are few statements you copy and
# pasted it multiple times inside the function
# its good to convert those statements to inner function

# def sum(a, b):
#   return a + b
# function without name is also caled annonymous function
# however if the function do not have a name how to call / invoke them
# based on our diagram can we write function as
# sum = def(a, b):
#    return a + b

# functions are executed in the main context
# in other words functions can see the variable created in the main context
x = 10
def sayX():
    print(x)

sayX()

# however python still has lambda function
# lambda function can have only one statement
# lambda functions are written in one line
def add(x, y):
    return x + y
# Step 1: convert your function to an annonymous function
# def (x, y): return x + y
# Step 2: We cannot call the no name function (annonymous function)
# let us assign the function to a variable
# sum = def (x, y): return x + y
# Step 3: rename def with lambda
# sum = lambda (x, y): return x + y
# Step 4: parenthesis "()" and "return" keyword can be remove
sum = lambda x, y: x + y
print(add(10, 20))
print(sum(10, 20))

fahrenheitvalues = [32, 33, 34, 35, 36, 37, 38, 39, 40]

def convertFahrenheitToCelsius(fahrenheitvalue):
    return (fahrenheitvalue - 32) * 5/9
celsiusvalues = map(convertFahrenheitToCelsius, fahrenheitvalues)
print("Celsius Values using map:", list(celsiusvalues))

celsiusvalues = map(lambda value: (value - 32) * 5/9, fahrenheitvalues)
print("Celsius Values using map:", list(celsiusvalues))