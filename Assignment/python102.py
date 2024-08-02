
## Exercise 1: Check Even or Odd
'''
Write a Python program that takes an integer as input and checks whether it is even or odd.
'''
'''
num = input("Please key in any number: ")

if ((int(num) % 2) == 0):
  print("This is an even number")
else:
  print("This is an odd number")

print("Thank you")
'''



## Exercise 2: Grade Evaluation**
'''
Write a Python program that takes a score (between 0 and 100) as input and prints the corresponding grade based on the following criteria:

A for scores 90 and above
B for scores 80-89
C for scores 70-79
D for scores 60-69
F for scores below 60
'''
'''
grade = input("Please key in your score: ")

if (int(grade) >= 90):
  print("Your score is Grade A")
elif (int(grade) >= 80 and int(grade) <= 89):
  print("Your score is Grade B")
elif (int(grade) >= 70 and int(grade) <= 79):
  print("Your score is Grade C")
elif (int(grade) >= 60 and int(grade) <= 69):
  print("Your score is Grade D")
else:
  print("Your score is Grade F")

print("Thank You")
'''



## Exercise 3: Check Leap Year
'''
Write a Python program that takes a year as input and checks whether it is a leap year.
'''
'''
year = input("Please enter the year: ")

if ((int(year) % 4 == 0) & ((int(year) % 100 == 0) | (int(year) % 400 == 0))):
  print(f"{year} is likely a leap year")
else:
  print(f"{year} is not a leap year")

print("Have a good year of 2024!")

'''



## Exercise 4:  Number Comparison
'''
Write a program that takes three numbers as input and prints the largest one.
'''
'''
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
third_num = int(input("Enter third number: "))

if (first_num >= second_num) and (first_num >= third_num):
  print(f"{first_num} is the largest number")
elif (second_num >= first_num) and (second_num >= third_num):
  print(f"{second_num} is the largest number")
else:
  print(f"{third_num} is the largest number")

print("Have a great day!")
'''



## Exercise 5: Check Vowel or Consonant
'''
Write a Python program that takes a single character as input and checks whether it is a vowel or consonant.
'''
'''
letter = str(input("Enter an alphabet: "))

if (letter == 'a'):
  print("'a' is a vowel")
elif (letter == 'e'):
  print("'e' is a vowel")
elif (letter == 'i'):
  print("'i' is a vowel")
elif (letter == 'o'):
  print("'o' is a vowel")
elif (letter == 'u'):
  print("'u' is a vowel")
else:
  print(f"'{letter}' is a consonant")

print("You are amazing!")
'''



## Exercise 6: BMI Calculator
'''
Write a program that calculates the Body Mass Index (BMI) and categorizes it into different weight statuses. The formula for BMI is weight / height^2, where weight is in kilograms and height is in meters.

Categories:
Underweight: BMI < 18.5
Normal weight: 18.5 <= BMI < 24.9
Overweight: 25 <= BMI < 29.9
Obesity: BMI >= 30
'''
'''
weight = input("Please state your weight(kg): ")
height = input("Please state your height(m): ")

bmi = float(weight) / float(height) ** 2
if (bmi < 18.5 ):
  print("You are underweight.")
elif (bmi >= 18.5 and bmi < 24.9):
  print("Your weight are normal.")
elif (bmi >= 25 and bmi < 29.9):
  print("You are overweight.")
else:
  print("Your weight is obesity.")

print("Thank You")
'''



## Exercise 7: Triangle Type Checker
'''
Write a program that takes the lengths of three sides of a triangle and 
determines whether the triangle is equilateral, isosceles, or scalene.

Equilateral: All three sides are equal.
Isosceles: Exactly two sides are equal.
Scalene: All three sides are different.
'''
'''
print("Hi, let me help you to determine types of triangle")
a = input("Please state the first length: ")
b = input("Please state the second length: ")
c = input("Please state the third length: ")

if (int(a) == int(b) and int(b) == int(c) and int(a) == int(c)):
  print("Therefore, this is an equilateral triangle.")
elif (int(a) == int(b) or int(b) == int(c) or int(a) == int(c)):
  print("Therefore, this is an isosceles triangle.")
else:
  print("Therefore, this is a scalene triangle.")

print("Thank You")
'''



## Exercise 8: ATM Withdrawal
'''
Write a program that simulates an ATM withdrawal. The user enters the withdrawal amount and 
the program checks if the amount is a multiple of 10. If it is, the program prints the 
number of each denomination (50, 20, 10) required to dispense the amount. If not, 
it prints an error message. For example if the amount is 233 then it must print "4 50 
dollar bills, 1 20 dollar bills, 1 10 dollar bills, 3 1 dollar bills
'''
'''
amt = int(input("Please enter the withdrawal amount: "))

if (amt % 10 == 0 and amt == amt):
    amt_50 = amt % 50
    withdraw_50 = amt // 50
    amt_20 = amt_50 % 20
    withdraw_20 = amt_50 // 20
    amt_10 = amt_20 % 10
    withdraw_10 = amt_20 // 10

    print(f"RM 50 x {withdraw_50}")
    print(f"RM 20 x {withdraw_20}")
    print(f"RM 10 x {withdraw_10}")
else:
    print(f"Error: You requested an amount that cannot be dispensed")

print("Thank you")
'''



## Exercise 9: Adam Number
'''
Write a Python program to check whether a given number is an Adam number.

An Adam number is a number for which the square of the number and the square of 
its reverse are themselves reverses of each other. In other words, if you take a 
number, reverse it, square both the original number and the reversed number, and the
 results are still reverse of each other, then the original number is called an Adam number.
'''
'''
x = str(input("Please enter the 2 digits number: "))

y = x[::-1]

square_x = str(int(x) ** 2)
reversed_square_x = square_x[::-1]
square_y = str(int(y) ** 2)

if (reversed_square_x == square_y):
  print(f"Squared number = {square_x}")
  print(f"Reversed number = {y}")
  print(f"Squared of reversed number = {square_y}")
  print(f"Therefore, {x} is an Adam number")
else:
  print(f"Squared number = {square_x}")
  print(f"Reversed number = {y}")
  print(f"Squared of reversed number = {square_y}")
  print(f"Therefore, {x} is an Adam number")

print("Thank you")
'''



## Exercise 10: Armstrong Number
'''
Write a Python program to check whether a given number is an Armstrong number.
An Armstrong number (also known as a Narcissistic number or a Pluperfect number) is 
a number that is equal to the sum of its own digits each raised to the power of the 
number of digits. For example, 153 is an Armstrong number because 
1 ** 3 + 5 ** 3 + 3 ** 3 = 153
'''
'''
num = 153

result1 = num % 10
num1 = num // 10
result2 = num1 % 10
num2 = num1 // 10
result3 = num2 % 10
num3 = num2 // 10

total = (result3 ** 3) + (result2 ** 3) + (result1 ** 3)

if (num == total):
  print(f"Since {num} = {result3}^3 + {result2}^3 + {result1}^3")
  print(f"Therefore, {num} is an armstrong number.")
else:
  print(f"Since {num} =! {result3}^3 + {result2}^3 + {result1}^3")
  print(f"Therefore, {num} is not an armstrong number.")

print("Thank you")
'''