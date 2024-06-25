# Function are not for solving problems like operators, if, for, while
# Function are used to organize our code
# When to create our own function?
# Whenever you copy and paste a block of code
# then you know already it has to be a function
# remember the first code we did in python is
def sayHelloworld():
    print("Hello world inside the function!!!")


# Declaring a function
# The above statement can we just write as 1 line
# or do we have to create a function put this line inside the
# function and call the function
# well, it depends on your requirement
# Lets say if you copy this lien and paste it in 5 places
# then it must be converted a function
# which is agin followed by colon :
# place your block of code inside the function with indentation

# Calling a function
# what will happen if we never call/invoke the function
# Nothing happens the code inside the function never gets executed
# functions are created using the keyword def
# function name followed by paranthesis ()
sayHelloworld()

# when we create a function if that function takes some value
# then we must create a variable (placeholder) in between the bracket
# if the function takes more than 1 value then we must create
# more than 1 variable(s) (placeholders) separated by comma
# these variable(s) is called "paremeter"

def greeting(name):
    print("Good morning Ma'am")

# if the parameter is dull colour then it means we are taking parameter
# but not using that parameter inside the function

def greeting(name):
    print("Good morning", name)

# When we call the function since the function is taking a parameter(s)
# we must pass value to the parameter(s)
# the value we are pssing is called argument
# the number of argument(s) must match with number of parameter(s)
greeting("Beatrice")

def total(x, y, z):
    results = x + y + z
    print("Result:", results)

total(10, 20, 30)
# the arguments are positional

# for example i have this function and inside this function we have code
# to identify the price for each food and return the prices
# so that the caller can do the payment
def buyLunch(makan, minum):
    prices = []
    for food in makan:
        if (food == "nasi"):
            # append is a function inside the object prices (instance of list)
            # so append is a method
            prices.append(2.80)
        elif (food == "sayur"):
            prices.append(2.20)
    for food in minum:
        if (food == "nescafe"):
            prices.append(2.50)
    # print(prices)
    return prices

# now calculate the amount to be paid
# unless the function return/give you back the receipt
# there is no way for us to find the amount to be paid
# since the buyLunch function is returning some value
# it becomes compulsory for us the hold the value
# we must declare the placeholder
itemPrices = buyLunch(["nasi", "sayur"], ["nescafe"])
total = 0
for price in itemPrices:
    total = total + price
print("Amount to be paid: ", total)

# whether th return value must be a list
def simpleInterest(principle, period, rate):
    interest = (principle * period * rate) / 100
    # return [interest, principle, period, rate]
    return interest

print("Interest Amount: ", simpleInterest(1000, 1, 6))

# however when you return more than one value separated by comma
# it will be a tuple (tuple is nothing but read only list)
def participantList(nameone, nametwo, namethree):
    nameone = nameone + "Machine Learning"
    nametwo = nametwo + "Machine Learning"
    namethree = namethree + "Machine Learning"
    return nameone, nametwo, namethree

result = participantList("John", "Peter", "Matthew")
print(type(result))

# you can also make the parameter(s) optional by having a default value
def calculateSimpleInterest(principle, period, rate=6):
    interest = (principle * period * rate) / 100
    return interest

# since we are not passing the value for rate parameter
# the period will automatically become 1 and the rate will automatically become 6
#print(calculateSimpleInterest(1000))
# now the second argument is passed which means periods becomes 2 and rate becomes 6
# which means the arguments are stil positional
print(calculateSimpleInterest(1000, 2))

# is there a way values for principle and rate only
# we can use something called "Named Argument / Keyword Argument"
# the name is referring to parameter
#print(calculateSimpleInterest(principle=1000, rate=6))

def findTotal(givenNumbers):
    total = 0
    for givenNumber in givenNumbers:
        total = total + givenNumber
    return total

# Variable length Argument
# the number of arguments which we pass vary
# caller can pass the values as a list
print(findTotal([10, 20, 30]))
print(findTotal([10, 20, 30, 40, 50, 60]))
print(findTotal([10, 20, 30, 40, 50, 60, 70, 80, 90]))

# but there are use cases where the caller is not able to place the
# values inside the list and pass the list
# you can declare the parameter to be able to accept any number
# by introducing * infront of the parameter
# python will take all the arguments place them inside a list
# and pass the list to the function
def calculateTotal(givenNumbers):
    total = 0
    for givenNumber in givenNumbers:
        total = total + givenNumber
    return total

print(calculateTotal([10, 20, 30]))
print(calculateTotal([10, 20, 30, 40, 50, 60]))
print(calculateTotal([10, 20, 30, 40, 50, 60, 70, 80, 90]))

def listSixLetterFruits(*fruits):
    for fruit in fruits:
        if len(fruits) == 6:
            print(fruit)

# we are sending the items/fruits individually (not as a list)
# however, python will convert them to a list of fruits and pass it
listSixLetterFruits("apple", "orange", "mango", "banana", "durian", "grapes")

def listFruitDetails(*fruits):
    for fruit in fruits:
        print(fruit)

listFruitDetails("apple", 20, 1.40, "orange", 40, 1.20)