
## Problem 1:
'''
Print first 10 natural numbers using while loop
'''
'''
number = 0
natural_num = []

while (number < 10):
  number += 1
  natural_num.append(number)

print(natural_num)
'''



## Problem 2:
'''
Print first 10 prime numbers using for loop
'''
'''
num = range(2, 51)

for i in num:
    isPrime = True
    divisors = range(2, i)
    for j in divisors:
        if (i % j == 0):
            isPrime = False
            break
    if (isPrime == True):
        print(i)
'''



## Problem 3:
'''
Get number of items as input and generate that many ADAM Numbers
'''
'''
num_items = int(input("Enter the ADAM number that you want to generate: "))

count = 0
number = 1
adam_num = []
while (count < num_items):
  square = number ** 2
  reverse_num = int(str(number)[::-1])
  reverse_square = int(str(square)[::-1])
  if (reverse_square == reverse_num ** 2):
    adam_num.append(number)
    count += 1
  number += 1

print(f"The first {num_items} list of ADAM numbers are {adam_num}")
'''



## Problem 4:
'''
Get number of items as input and generate that many Armstrong Numbers
'''
'''
num_items = int(input("Enter the Armstrong numbers that you want to generate: "))

armStrong = []
number = 0

while len(armStrong) < num_items:
    digits = list(map(int, str(number)))
    num_digits = len(str(number))
    total = 0
    for digit in digits:
        sum_of_power = digit ** num_digits
        total += sum_of_power

    if number == total:
      armStrong.append(number)
    number += 1

print(f"The first {num_items} list of ADAM numbers are {armStrong}")
'''



## Problem 5:
'''
Write a program to print the following pattern using a loop.
o
oo
ooo
oooo
ooooo
'''
'''
iterate = 5

for x in range (1, iterate +1):
  print("o" * x)
'''



## Problem 6:
'''
Write a program to print the following pattern using a loop

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
'''
number = 5

for x in range(1, number + 1):
  for y in range (1, x + 1):
    print(y, end=" ")
  print()
'''




## Problem 7:
'''

Get a number as input and calculate the sum of all numbers from 1 to the given number.

'''
'''
number = int(input("Enter a number: "))

sum = 0

for x in range(1, number + 1):
  sum += x
print(f"The sum of all numbers from 1 to {number} is {sum}")

'''



## Problem 8:
'''
Write a python program that takes few numbers as command line argument. Use a loop to 
display all elements. Use another loop to display all elements in the even position. 
Use another loop to display all elements in the odd position.
'''
'''
import sys
number_list = '',join(sys.argv[1:])

print("The even numbers are ")
for i in range(2, len(number_list), 2):
  print(number_list[i], end=' ')
print()

print("The odd numbers are ")
for i in range(1, len(number_list), 2):
  print(number_list[i], end=' ')
print()
'''



## Problem 9:
'''
Write a python program that takes few numbers as command line argument. 
Find the average of those numbers.
'''
'''
import sys
number_list = sys.argv

sum = 0

for num in number_list[1:]:
  sum = sum + int(num)

mean = sum / (len(number_list)-1)
print(mean)
'''



## Problem 10:
'''
Write a Python program that takes a string as input, which contains numbers separated 
by commas. Convert the string to a list of numbers and determine whether all the 
numbers are different from each other.
'''
'''
number_list = str(input("Enter numbers separated by commas: "))

number_list = number_list.split(',')

if (len(number_list)) == len(set(number_list)):
  print("All the numbers are different")
else:
  print("There are duplicate number")
'''



## Problem 11:
'''
Write a Python program that takes a string as input, which contains numbers separated 
by commas. Convert the string to a list of numbers. Now pick 3 unique numbers from 
the list whose sum is 100.
'''
'''
numList = input("Enter numbers with the usage of commas: ")

strNumList = numList.split(",")
numInList = [int(num) for num in strNumList]
uniqueNum = set()

unik = False
for num in numInList:
    if num < 100:
        uniqueNum.add(num)

a = sorted(uniqueNum)
for x in range(len(a)):
    for y in range(x+1, len(a)):
        for z in range(y+1, len(a)):
            sum = a[x] + a[y] + a[z]
            if sum == 100:
                unik = True
                print(f"The three number that sum to 100 are: {a[x]}, {a[y]}, {a[z]}")

if not unik:
    print("No combination of three numbers sums to 100")
'''



## Problem 12:
'''
Write a Python program to get 2 positive numbers as input and multiply them 
without using the '*' operator.
'''
'''
num_1 = int(input("Enter first positive number: "))
num_2 = int(input("Enter second positive number: "))

total = 0
for i in range(num_2):
  total += num_1
print(f"Product of {num_1} and {num_2} is {total}")
'''




## Problem 13:
'''
Write a python program to print first 10 terms in a Fibonacci series
'''
'''
first_num, second_num = 0, 1

for i in range(11):
  print(first_num, end=' ')
  first_num, second_num = second_num, first_num + second_num

print()
'''



## Problem 14:
'''
Write a python program which takes a number as input and convert the 
number to binary. Note: Don't use any builtin functions.
'''
'''
number = int(input("Enter a number: "))

binary = []

while (number > 0):
  remainder = number % 2
  binary.append(remainder)
  number = number //2

binary.reverse()

for i in binary:
  print(i)
'''



## Problem 15:
'''
Write a python program which takes a binary number as input and convert the 
number to decimal. Note: Don't use any builtin functions.
'''
'''
binary = str(input("Enter a binary number: "))

sum = 0
exponent = 0
for digit in reversed(binary):
  sum += int(digit) * (2** exponent)
  exponent += 1

print(sum)
'''