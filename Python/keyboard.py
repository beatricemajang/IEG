# python has a built in function called input
# the input function takes a single parameter (caption/question)
# Input function will display the caption
# and wait for the user input
# the user will provide the input and press enter key
# whatever the user provide will be stored in a avariable
firstNumber = input("Please key in the first number: ")
print(firstNumber)
# the input is always of type string
print(type(firstNumber))

secondNumber = input("Please key in the second number: ")
print(firstNumber + secondNumber) # string concatenation
print(int(firstNumber) + int(secondNumber)) # addition

numbers = input("Enter the number to do Total: ")
number_list = numbers.split(",")
print(number_list)
total = 0
for number in number_list:
    # int function trim the string value
    # remove the spaces in the string and then convert
    # string to integer
    total = total + int(number)
print(total)