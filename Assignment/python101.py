
## Exercise 1: Basic Arithmetic Operations
'''
Write a Python program that does the following:
Prompts the user to enter two numbers. Stores these numbers in two variables. 
Performs and prints the results of addition, subtraction, multiplication, 
and division of these two numbers.
'''
'''
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

print("Addition: ", first_num + second_num)
print("Subtraction: ", first_num - second_num)
print("Multiplication: ", first_num * second_num)
print("Division: ", first_num / second_num)
'''



## Exercise 2: Temperature Converter
'''
Write a Python program that:
Prompts the user to enter a temperature in Celsius. 
Converts the temperature to Fahrenheit. Prints the temperature in Fahrenheit. 
(Hint: The formula to convert Celsius to Fahrenheit is: F = C * 9/5 + 32)
'''
'''
celsius_num = int(input("Enter a temperature number: "))

fahrenheit_value = celsius_num * 9/5 + 32

print("Therefore, the Fahrenheit is ", fahrenheit_value)
'''



## Exercise 3: Area and Perimeter of a Rectangle
'''
Write a Python program that:
Prompts the user to enter the length and width of a rectangle. 
Calculates the area and perimeter of the rectangle. Prints the area and perimeter.
'''
'''
length_value = int(input("Length value of a rectangle: "))
width_value = int(input("Width value of a rectangle: "))

print("Area: ", length_value * width_value)
print("Perimeter: ", (length_value * 2) + (width_value * 2))
'''



## Exercise 4: Simple Interest Calculator
'''
Write a Python program that:
Prompts the user to enter the principal amount, rate of interest, and time in years. 
Calculates the simple interest. Prints the simple interest. 
(Hint: The formula to calculate simple interest is: SI = (P * R * T) / 100)
'''
'''
principal_amount = float(input("Enter principal amount: "))
rate_interest = float(input("Enter rate of interest: "))
time_years = int(input("Enter time in years: "))

si = (principal_amount * rate_interest * time_years) / 100

print("Simple Interest: ", si)
'''



## Exercise 5: Swapping Two Variables
'''
Write a Python program that:
Prompts the user to enter two numbers. Swaps the values of the two variables. 
Prints the values before and after swapping.
'''
'''
first_num = str(input("Enter first number: "))
second_num = str(input("Enter second number: "))

before_swap =  first_num + second_num
after_swap = second_num + first_num

print("Before swapping: ", before_swap)
print("After swapping: ", after_swap)
'''



## Exercise 6: Square and Cube
'''
Write a Python program that:

Prompts the user to enter a number. Calculates the square and cube of the number. 
Prints the square and cube.
'''
'''
num = input("Enter first number: ")

print("Square of the number: ", int(num) ** 2)
print("Cube of the number: ", int(num) ** 3)
'''



## Exercise 7: Calculate BMI
'''
Write a Python program that:
Prompts the user to enter their weight in kilograms and height in meters. 
Calculates the Body Mass Index (BMI). Prints the BMI. 
(Hint: The formula to calculate BMI is: BMI = weight / (height * height))
'''
'''
kilos = input("What is your weight (kg): ")
height = input("What is your height (m): ")

print("Your BMI is ", float(kilos)/ (float(height) * float(height)))
'''



## Exercise 8: Compound Interest Calculator
'''
Write a Python program that:

Prompts the user to enter the principal amount, rate of interest, time in years, 
and number of times interest is compounded per year. Calculates the compound interest. 
Prints the compound interest.
(Hint: The formula to calculate compound interest is: A=P(1+R/100n)nt
where A is the amount, P is the principal amount, R is the annual interest rate, 
t is the time the money is invested for, and n is the number of times interest is compounded per year)
'''
'''
principal_amount = input("Enter the principal amount: ")
rate_interest = input("Enter the annual rate of interest: ")
money_invested = input("Enter the time money invested: ")
time_interest = input("Enter the number of times interest: ")

A = float(principal_amount) * (1 + float(rate_interest) / 100 * int(time_interest)) * int(time_interest) * float(money_invested)

print("Simple Interest: ", A)
'''



## Exercise 9: Convert 97409 to Binary
'''
Write a Python program that:
Converts the given integer 97409 to its binary representation. 
Prints the binary representation.
'''
'''
a0 = 97409
print(a0)

b1 = a0 % 2
a1 = a0 // 2
print(b1, a1)

b2 = (a1 % 2)
a2 = a1 // 2
print(b2, a2)

b3 = (a2 % 2)
a3 = a2 // 2
print(b3, a3)

b4 = (a3 % 2)
a4 = a3 // 2
print(b4, a4)

b5 = (a4 % 2)
a5 = a4 // 2
print(b5, a5)

b6 = (a5 % 2)
a6 = a5 // 2
print(b6, a6)

b7 = (a6 % 2)
a7 = a6 // 2
print(b7, a7)

b8 = (a7 % 2)
a8 = a7 // 2
print(b8, a8)

b9 = (a8 % 2)
a9 = a8 // 2
print(b9, a9)

b10 = (a9 % 2)
a10 = a9 // 2
print(b10, a10)

b11 = (a10 % 2)
a11 = a10 // 2
print(b11, a11)

b12 = (a11 % 2)
a12 = a11 // 2
print(b12, a12)

b13 = (a12 % 2)
a13 = a12 // 2
print(b13, a13)

b14 = (a13 % 2)
a14 = a13 // 2
print(b14, a14)

b15 = (a14 % 2)
a15 = a14 // 2
print(b15, a15)

b16 = (a15 % 2)
a16 = a15 // 2
print(b16, a16)

b17 = (a16 % 2)
a17 = a16 // 2
print(b17, a17)

print(str(b17)+str(b16)+str(b15)+str(b14)+str(b13)+str(b12)+str(b11)+str(b10)+str(b9)+str(b8)+str(b7)+str(b6)+str(b5)+str(b4)+str(b3)+str(b2)+str(b1))
'''



## Exercise 10: Convert 1011 to Decimal
'''
Write a Python program that:
Converts the given binary 1011 to its decimal representation. 
Prints the decimal representation.
'''
'''
b0 = 1011

d1 = (2 ** 0) * (b0 % 10)
b1 = b0 // 10
print(d1, b1)

d2 = d1 + (2 ** 1) * (b1 % 10)
b2 = b1 // 10
print(d2, b2)

d3 = d2 + (2 ** 2) * (b2 % 10)
b3 = b2 // 10
print(d3, b3)

d4 = d3 + (2 ** 3) * (b3 % 10)
b4 = b3 // 10
print(d4, b4)
print(f"Hence, the decimal is {d4}")
'''