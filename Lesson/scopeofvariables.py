# Only in python the function can access the variable
# declared in the main context
x = 10

def sayX():
    print(x) # usually x is initialized and then only used
    # in this case "funciton can see x in main context"

sayX()  # 10

def modifyX():
    x = 20
    # whenever you modify the variable which is in the global context
    # the variable is initialized locally
    # in this case x automatically become local variable
    print(x)

modifyX() # 20
print(x) # 10

# What if I don't want to create x as local variable
# In other words after I call the function 
# my global variable change its value
def changeX():
    global x # telling python for variable x refer the main context
    # in other words we are saying dont create x as local variable
    print(x) # we are referring to the global x
    x = 20 # you change the value of global x permanently

changeX() # 20
print(x) # 20
# Summary: Since I use the global keyword inside my function
# my function is able to change the value of x which is in global context


def authenticate(): # outer function
    result = 11111
    def simpleInterest(): # inner function
        nonlocal result # strictly use the result declared in the outer function
        result = 22222 # now it become local variable (since we are trying to modify it)
        print(result) # we are looking at a variable which is in the outer function
    simpleInterest()
    print(result)

authenticate()
