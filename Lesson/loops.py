# whenever you want to iterate a list of items then you must use for loop
fruits = ["apple", "rambutan", "orange", "durian", "mango", "cempedak", "banana", "mangosteen", "grapes"]
# print all the items in the list
for fruit in fruits:
    print(fruit)

# print all the items in the even position
for fruit in fruits[::2]:
    print(fruit)

# print only fruit with 6 letters
for fruit in fruits:
    if (len(fruit) == 6):
        print(fruit)

# I want to print each fruit together with the index
position = 0
for fruit in fruits:
    print(position, fruit)
    position += 1

# I want to create a multiplicator table of 5
# I want to go until 12
multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
multiplicant = 5
for multiplier in multipliers:
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)

# however, this is not practical when the until is 200 instead of 12
# we have to go for range option start_index:end_index
# but the (:) operator can work only on array on the list[2:5]
# we have an built in function called range which can generate list of numbers
# range function takes start index and end index and genarate
# numbers between them
# start index is included end index is not included
print(range(1, 12)) 
# however when I print it, I am not able to see the numbers

# range is an iterable object, which means we can use it in for loops together 
# with "in" operator. However, print() function do not understand how to iterate
# them, so it prints as range(1, 12)
# any iterable object can be typecast to a list usin list function
# print function knows how to iterate the list

print(list(range(1, 12)))

# let us do the multiplication table using range
multiplicant = 6
for multiplier in range(1, 13):
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)

# split the digits in the input number and print them
# lets saythe user give input 97409
# take the input and print 9, 7, 4, 0, 9
# since we do not have it as a list and we also do not know the number of digits
# we have to use while loop
# given_num = input("Give me the number: ")
given_num = 97409
while (given_num > 0):
    print(given_num % 10)
    given_num //= 10

given_num = 12345
number_of_digit = len(str(given_num)) - 1
while (given_num > 0):
    print(given_num // 10 ** number_of_digit)
    given_num %= 10 ** number_of_digit
    number_of_digit -= 1

given_num = 67891
str_given_num = str(given_num)
for digit in str_given_num:
    print(digit)

# for loop and while loop  can have else block
fruits = ["apple", "orange", "mango", "banana", "grapes"]
# the code in the else block will get executed when all the fruits are iterated
# list iteration is exhausted (no more product to iterate)
for fruit in fruits:
    print(fruit)
    # since we added this condition now when it sees mango
    # jumps out of the loop (list iteration is not exhausted)
    # the code in the else block not executed
    if (fruit == "mango"): break
else:
    print("All fruits printed")

# Code in the else block gets executed only when the condition fails
multiplicant = 9 
multiplier = 1
while (multiplier <= 12):
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)
    multiplier += 1
    # since we added this condition now when it sees 11
    # jumps out of the loop (condition not fail yet 11 <= 12 true)
    # the code in the else block not executed
    if multiplier == 11: break
else:
    print("Multiplication table done")

# please do not print when multipliers are multiples of 5
# in other words do not print 5 x 10 = 50
multiplicant = 10 
multipliers = range(1, 13)
for multiplier in multipliers:
    if multiplier % 5 == 0: continue
    # what continue keyword will do is
    # without executing the following line(s) it will jump back to the loop
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)

