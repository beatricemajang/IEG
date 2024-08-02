
## Problem 1:
'''
Write a python function that takes a number as parameter and prints the multiplication 
table of that number
'''
'''
def table(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)

multiply = table(5)
'''



## Problem 2:
'''
Write a simple python function that returns twin primes less than 1000. If two 
consecutive odd numbers are both prime then they are known as twin primes.
Pairs of primes that differ by 2. For example, 3 and 5, 5 and 7, 11 and 13, and 17 and 19 
are twin primes.
'''
'''
def find_twin_primes(n=1000):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [p for p in range(2, n) if is_prime(p)]
    odd_primes = [p for p in primes if p % 2!= 0]
    twin_primes = [(p, p + 2) for p in odd_primes if p + 2 in odd_primes]

    return twin_primes

print(find_twin_primes())
'''



## Problem 3:
'''
Write a simple python function that takes a number as parameter and returns the prime 
factors of that number. Prime Factorization is finding which prime numbers multiply 
together to make the original number.
Example: prime factors of 56 - 2, 2, 2, 7
'''
'''
def prime_factorization(n):
    if n < 2:
        return []
    if n == 2:
        return [2]

    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors

result = prime_factorization(56)
product = 1
for j in result:
    product *= j
print(f"{result} = {product}")
'''



## Problem 4:
'''
Write a function that inputs a number and returns the product of digits of that number.
'''
'''
def product_of_digits(num):
    product = 1
    while num > 0:
        product *= num % 10
        num //= 10
    return product

num = int(input("Enter a 3 digits number: "))
result = product_of_digits(num)
print(result)
'''



## Problem 5:
'''
Write a function that takes a number as parameter. The function finds the proper divisors 
of that number and then finds the sum of proper divisors. Proper divisors of a number are 
those numbers by which the number is divisible, except the number itself.
For example proper divisors of 36 are 1, 2, 3, 4, 6, 9, 18
'''
'''
def proper_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

num =int(input("Enter a number: "))
results = proper_divisors(num)
print(f"Proper divisors of {num} are {results}")
'''



## Problem 6:
'''
A number is called perfect if the sum of proper divisors of that number is equal to the 
number. For example 28 is perfect number, since 1+2+4+7+14=28. Write a program to print all 
the perfect numbers in a given range
'''
'''
def is_perfect(n):
    sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i
            if i * i != n:
                sum += n // i
    return sum == n

for i in range(1, 500):
    if is_perfect(i):
        print(i)
'''




## Problem 7:
'''
Write a python function that takes 2 parameters lower and upper (range). Let the function 
returns pairs of amicable numbers in that range.
Two different numbers are called amicable numbers if the sum of the proper divisors 
of each is equal to the other number. For example 220 and 284 are amicable numbers.
For example if we call that function: amicableNumbers(1, 1000)
The function must return: [220, 284]
Why they are amicable numbers ?
Sum of proper divisors of 220 = 1+2+4+5+10+11+20+22+44+55+110 = 284
Sum of proper divisors of 284 = 1+2+4+71+142 = 220
'''
'''
def sum_of_proper_divisors(n):
    sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i * i != n:
                sum += i + n // i
            else:
                sum += i
    return sum

def amicable_numbers(lower, upper):
    amicable_numbers = []
    for i in range(lower, upper + 1):
        sum_of_proper_divisors_i = sum_of_proper_divisors(i)
        if sum_of_proper_divisors_i != i and i < sum_of_proper_divisors_i <= upper:
            sum_of_proper_divisors_j = sum_of_proper_divisors(sum_of_proper_divisors_i)
            if sum_of_proper_divisors_j == i:
                amicable_numbers.append((i, sum_of_proper_divisors_i))
    return amicable_numbers

result = amicable_numbers(1, 10000)
print(result)
'''



## Problem 8:
'''
Write a python function that takes variable length parameters and returns maximum and 
minimum number in the parameter numbers.
For example if we call the function: maximumMinimum(10, 20, 30, 40, 50)
The function must return: [10, 50]
'''
'''
def max_min(*numbers):
    max = numbers[0]
    min = numbers[0]
    for i in numbers:
        if i > max:
            max = i
            if i < min:
                min = i
    return min,max

result = max_min(10, 20, 30, 40, 50)
print(result)
'''



## Problem 9:
'''
Write a simple Python function that takes a number(n) as a parameter. Then the function 
prints out the first n rows of Pascal's triangle. Note : Pascal's triangle is an 
arithmetic and geometric figure first imagined by Blaise Pascal.
'''
'''
def pascal(n) :
    triangle = {}
    for m in range(0, n) :
        listinrow = []
        for i in range(0, m + 1) :
            listinrow.append(str(binomial(m,i)))
        triangle[m] = listinrow
    pascaltolist(triangle)

def pascaltolist(t):
    width = len(t) *3
    for i in range(0, len(t)):
        my_string = ' '.join(t[i])
        padding = " " * ((width - len(my_string)) // 2)
        print(f"{padding}{my_string}{padding}")

def binomial(n, m) :
    count = 1
    if (m > n - m) :
        m = n - m
    for i in range(0, m):
        count = count * (n - i) // (i + 1)
    return count

pascal(8)
'''



## Problem 10:
'''
Write a simple python function that accepts a hyphen-separated sequence of words as 
parameter and returns the words in a hyphen-separated sequence after sorting them 
alphabetically.

Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
'''
'''
def hyphen_sort(colour):
    colour = colour.split("-")
    colour.sort()
    return "-".join(colour)

colour = "green-red-yellow-black-white"
print(f"Sample Items: {colour}")
print(f"Result: {hyphen_sort(colour)}")
'''