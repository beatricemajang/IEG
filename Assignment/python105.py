
## Problem 1 FizzBuzz:
'''
Write a program that prints the numbers from 1 to 100. But for multiples of three, 
print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For 
numbers which are multiples of both three and five, print "FizzBuzz".
'''
'''
for i in range(1, 101):
  if i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  elif (i % 3 == 0) or (i % 5 == 0):
    print("Fizbuzz")
  else:
    print(i)
'''



## Problem 2 Collatz Sequence:
'''
Write a program that takes an integer input from the user and generates the Collatz 
sequence for that number. The Collatz sequence is defined as follows:

start with a number n. If n is even, the next number is n/2. If n is odd, the next 
number is 3n + 1. Repeat the process until n becomes 1.
'''
'''
num = int(input("Enter an integer: "))

def collatz_sequence(n):

  sequence = []
  while n != 1:
    sequence.append(n)
    if n % 2 == 0:
      n = int(n/2)
    else:
      n = int(3 * n + 1)
  sequence.append(1)
  return sequence

print(f"Collatz sequence =", collatz_sequence(num))
'''



## Problem 3 GCD Calculation:
'''
Write a program that takes two integers from the user and calculates their greatest 
common divisor (GCD) using the Euclidean algorithm.

You can refer this Link

https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
'''
'''
num_1 = int(input("Enter first integer: "))
num_2 = int(input("Enter second integer: "))

def gcd(num_1,num_2):
  while num_2 != 0:
    num_1, num_2 = num_2, num_1 % num_2
  return num_1

statement = f"GCD({num_1},{num_2}) = {gcd(num_1,num_2)}"
print(statement)
'''



## Problem 4 Rock, Paper, Scissors:
'''
Write a program that plays the game of Rock, Paper, Scissors with the user. The user 
makes a choice, the program randomly chooses, and the winner is determined.
To generate random number use random module
import random
random.randint(1,3)
'''
'''
import random

def game_choice():
  num = random.randint(1, 3)
  if "rock" == 1:
    return "rock"
  elif "paper" == 2:
    return "paper"
  else:
    return "scissors"

def who_is_winner(user_option, my_option):
  if user_option == my_option:
    return "It's a tie!"
  elif (user_option == 'rock' and my_option == 'paper') or \
       (user_option == 'rock' and my_option == 'scissors') or \
       (user_option == 'paper' and my_option == 'rock') or \
       (user_option == 'paper' and my_option == 'scissors') or \
       (user_option == 'scissors' and my_option == 'rock') or \
       (user_option == 'scissors' and my_option == 'paper'):
       return "You win!"
  else:
    return "I win! "

print("Rock, Paper or Scissors?\n")
user_option = str(input("You choose "))
my_option = game_choice()
print(f"I choose {my_option}")
result = who_is_winner(user_option, my_option)
print(f"Winner: {result}")
'''



## Problem 5 Number Guessing Game:
'''
Write a program that randomly generates a number between 1 and 100. The user has to guess 
the number. After each guess, the program tells the user whether the guess is too high, 
too low, or correct. The game continues until the user guesses the correct number.
To generate random number use random module
import random
random.randint(1,3)
'''
'''
import random
number = random.randint(1, 10)

while True:
  user_guess = int(input("Try to guess number between 1 to 10: "))
  if user_guess < number:
    print("Ops, too low! Try again")
  elif user_guess > number:
    print("Ops, too high! Try again")
  else:
    print('Well done, you guessed the correct number!')
    break

  print("Thanks for playing!")
'''



## Problem 6 Perfect Number:
'''
Write a program that generates 10 perfect numbers.
Example
6: The divisors of 6 are 1, 2, 3, and 6. The sum of its proper divisors 
(excluding 6 itself) is 1 + 2 + 3 = 6.
28: The divisors of 28 are 1, 2, 4, 7, 14, and 28. The sum of its proper divisors 
(excluding 28 itself) is 1 + 2 + 4 + 7 + 14 = 28.
'''
'''
def find_divisors(num):
    divisors = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != 1 and i != num // i:
                divisors.append(num // i)
    return divisors

def is_perfect_number(num):
    return sum(find_divisors(num)) == num

def generate_perfect_numbers(count):
    perfect_numbers = []
    num = 2  # Start checking from the first positive integer
    while len(perfect_numbers) < count:
        if is_perfect_number(num):
            perfect_numbers.append(num)
        num += 1
    return perfect_numbers

perfect_number = generate_perfect_numbers(4)
print(perfect_number)
'''




## Problem 7 Harmonic Series:
'''
Write a program that calculates the sum of the first n terms of the harmonic series. 
Take the n as Input.
Hn = 1 + 1/2 + 1/3 + 1/4 .... + 1/n
'''
'''
num = int(input("Enter a positive integer: "))

def harmonic_series(num):
  harmonic = 0
  for i in range(1, num + 1):
    harmonic += 1 / i
  return harmonic

result = harmonic_series(num)
print(f"The sum of the first {num} term of the harmonic series is {result:.2f}")
'''



## Problem 8 Number to Words:
'''
num = int(input("Enter a number range 0 to 1000: "))

ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = ["one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]

def num_to_words(num):
    if num < 10:
        return ones[num - 1]
    elif num < 20:
        return teens[num - 10]
    elif num < 100:
        return tens[num // 10 - 1] + ('' if num % 10 == 0 else '-' + ones[num % 10 - 1])
    elif num < 1000:
        return hundreds[num // 100 - 1] + ('' if num % 100 == 0 else ' and ' + num_to_words(num % 100))
    else:
        return "Out of range"

print(num_to_words(num))
'''



## Problem 9 Roman to Integer:
'''
Write a program to convert a Roman numeral to an integer and also convert integer to Roman numeral
'''
'''
user_select = int(input("Select (1) 'Roman numeral to Integer' or (2) 'Integer to Roman numeral: "))

def roman_to_int(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_values[char]
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value
    return total

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_numeral = ""
    for i in range(len(val)):
        while num >= val[i]:
            num -= val[i]
            roman_numeral += syb[i]
    return roman_numeral

if user_select == 1:
  roman = input("Enter a Roman numeral: ").upper()
  integer_value = roman_to_int(roman)
  print(f"The integer number for {roman} is {integer_value}.")
else:
  num = int(input(" Enter an Integer number:"))
  roman_num = int_to_roman(num)
  print(f"The roman numeral for {num} is {roman_num}.")
'''



## Problem 10 String Compression:
'''
Write a program to perform basic string compression using the counts of repeated characters 
(e.g., "aabcccccaaa" -> "a2b1c5a3").
'''
'''
user_input = str(input("Enter a string to compress: "))

compressed = []
count = 1

for i in range(1, len(user_input)):
  if user_input[i] == user_input[i - 1]:
    count += 1
  else:
    compressed.append(user_input[i - 1] + str(count))
    count = 1

compressed.append(user_input[-1] + str(count))
compressed_string = ''.join(compressed)

print(f"Compressed string = {compressed_string}")
'''