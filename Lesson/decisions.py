# write a program to find whether the given number is 
# positive, negative or Zero
# write a program to find whether our business is making, 
# loss or breakeven

expenses = 100
sales = 1100

# Objective 1: just say whether we are making profit (single condition)
# if (sales - expenses > 0)
if (sales > expenses):
    # block of code
    print("You are making profit")

# Objective 2: say say whether we are making profit or loss (2 conditions)
if (sales > expenses):
    # block of code
    print("You are making profit")
else:
    print("You are making losses")

print("Thank You")

# Objective 3: say say whether we are making profit or loss or breakeven(2 conditions)
if (sales > expenses):
    # block of code
    print("You are making profit")
else:
    if (sales == expenses):
        print("You are making breakeven")
    else: 
        print("You are making losses")

if (sales > expenses):
    # block of code
    print("You are making profit")
elif (sales == expenses):
        print("You are making breakeven")
else: 
        print("You are making losses")

print("Thank You")

# if the statement to be executed is not a block of code
# it is a single statement then we can write the if and statement
# in the same line

# find whether the given number is even 
givenNumber = 5
if (givenNumber % 2 == 0): print("Even Number")

# find whether the given number is even or odd
print("Even Number") if (givenNumber % 2 == 0) else print("Odd Number")

# find whether the given number is positive, negative or zero
givenNumber = 1
print("positive") if (givenNumber > 0) else print("negative") if (givenNumber < 0) else print("zero")