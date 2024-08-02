
## Problem 1:
'''

A laboratory technician always needs to prepare various solutions.
Coming Sunday, he has to create a 20-liter solution that is 35% salt by mixing two
available solutions. One solution (A) is 25% salt, and the other solution (B) 
is 50% salt. How many liters of each solution are required to achieve the desired 
concentration?
Coming Monday, he has to create an 8-liter solution that is 25% sugar by mixing 
two available solutions. One solution (A) is 15% sugar, and the other solution (B) 
is 40% sugar. How many liters of each solution are required to achieve the desired 
concentration?

Write a simple, generic Python program to assist the laboratory technician. 
The program must take all these numbers (20 liters, 35, 25, 50) as input and calculate 
the required liters of each solution and print them. Please note that the same program 
must work for the second problem as well (8 liters, 25, 15, 40).

The maximum stock for solution (A) and solution (B) is always 3 liter only. After 
calculating/printing the required quantity of A and B, throw proper message. For 
example, required quantity of solution (A) is less than 3 liter say "Solution (A) 
is available can proceed". If required quantity of solution (B) is greater than 3 
liter say "Solution (B) is not available, please order 1.3 liter now".

'''
'''
vol_total = int(input("Enter the volume: "))
sol_total = int(input("Enter the solution concentration: "))
sol_total /= 100
sol_a = float(input("Enter the solution (A): "))
sol_a /= 100
sol_b = float(input("Enter the solution (B): "))
sol_b /= 100

vol_a = int(((vol_total * sol_total) - (vol_total * sol_b)) / (sol_a - sol_b))
vol_b = int(vol_total - vol_a)

print(f"The volume of Solution A is {vol_a}-liter")
print(f"The volume of Solution B is {vol_b}-liter")

max_sol = 3
if (vol_a > max_sol and vol_b > max_sol):
  remain_a = float(vol_a - max_sol)
  remain_b = float(vol_b - max_sol)
  print(f"Solution (A) is not available, please order {remain_a} liter now.")
  print(f"Solution (B) is not available, please order {remain_b} liter now.")
elif (vol_a > max_sol and vol_b < max_sol):
  remain_a = float(vol_a - max_sol)
  print(f"Solution (A) is not available, please order {remain_a} liter now.")
  print("Solution (B) is available can proceed.")
elif (vol_a < max_sol and vol_b > max_sol):
  remain_b = float(vol_b - max_sol)
  print("Solution (A) is available can proceed.")
  print(f"Solution (B) is not available, please order {remain_b} liter now.")
else:
  print("Solution (A) and Solution (B) is available can proceed.")
'''



## Problem 2:
'''
Initialize two variables, x = 0b10101100 and y = 0b11011001.

Write Python code to:
1. Extract the lower 4 bits from x.
2. Check if y is even or odd.
3. Clear the upper 4 bits of x.
4. Check if the 5th bit of y is set.
'''
'''
# 1. extract the lower 4 bits from x
x = 0b10101100
mask = 0b00001111
print(f"1.", bin(x & mask))

# 2. check if y is even or odd
y = 0b11011001
print("2. y is an even number") if (y % 2 == 0) else print("2. y is an odd number")

# 3. clear the upper 4 bits of x
x = 0b10101100
mask = 0b00001111
print(f"3.", bin(x & mask))

# 4. check if the 5th bit of y is set
y = 0b11011001
mask = 0b00010000
result = y & mask
print("4. 5th bit of y is set") if result else print("4. 5th bit of y is not set")
'''



## Problem 3:
'''
A construction project requires two workers to complete. Worker A can complete the 
project in 12 hours, while Worker B can complete the same project in 16 hours. 
How long will it take for both workers to complete the project if they work together?

Another project requires Worker C, who can complete it in 8 hours, and Worker D, 
who can complete it in 10 hours. How long will it take for both workers to complete 
this project if they work together?

Write a simple, generic Python program to assist in calculating the time required for 
two workers to complete a project when working together. The program must take all 
these numbers (12, 16) as input and calculate the required time. Finally, print the 
result. Please note that the same program must work for the second problem as well (8, 10).
'''
'''
worker_a = int(input("The worker A to complete the project: "))
worker_b = int(input("The worker B to complete the project: "))

worker_ab = (1 / worker_a) + (1 / worker_b)
worker_ab = 1 / worker_ab

print(f"When worker A and Worker B work together, they will complete the project approximately {worker_ab:.2f} hours")
'''



## Problem 4:
'''
Initialize two variables, a = 0b10101000 and b = 0b01010100.

Write Python code to:
1. Set the lower 4 bits of a.
2. Combine the bits of a and b using OR.
3. Create a mask to set the 2nd and 6th bits of a.
'''
'''
a = 0b10101000
b = 0b01010100

# 1. set the lower 4 bits of a
mask_1 = 0b00001111
print("1. ", bin(a | mask_1))

# 2. combine the bits of a and b using OR
print("2. ",bin(a | b))

# 3. create a mask to set the 2nd and 6th bits of a
mask_3 = 0b10001010
print("3. ",bin(a ^ mask_3))
'''



## Problem 5:
'''
An investor decides to invest a total of RM30,000 in two different accounts. The 
first account offers a 5% annual interest rate, while the second account offers 
a 7% annual interest rate. If the total annual interest earned is RM1,800, how
 much money was invested in each account?

Another investor decides to invest a total of RM50,000 in two different accounts. 
The first account offers a 3% annual interest rate, while the second account offers 
a 6% annual interest rate. If the total annual interest earned is RM2,400, how much
 money was invested in each account?

Write a simple, generic Python program to assist in calculating the amount of money
invested in each account to achieve the desired total annual interest. The program 
must take all these numbers (30000, 5, 7, 1800) as input and calculate the required 
amounts. Finally, print the result. Please note that the same program must work for 
the second problem as well (50000, 3, 6, 2400).
'''
'''
total_invest = int(input("1. Enter total investment: "))
first_annual_interest = int(input("   Enter first annual interest rate: "))
first_annual_interest /= 100
second_annual_interest = int(input("   Enter second annual interest rate: "))
second_annual_interest /= 100
total_annual_invest = int(input("   Enter total annual investment: "))

second_invest = int((total_annual_invest - (first_annual_interest * total_invest)) / (second_annual_interest - first_annual_interest))
first_invest = total_invest - second_invest
print(f"   The money was invested in first account is RM {first_invest} and second account is RM {second_invest}")
'''



## Problem 6:
'''
Initialize two variables, x = 0b10101100 and y = 0b11010010.

Write Python code to:
1. Swap the values of x and y without using a temporary variable.
2. Toggle the 3rd and 5th bits of x.
3. Check if two given numbers a = 29 and b = 15 are different.
'''
'''
# 1. swap the values of x and y without using a temporary variable.
x = 0b10101100
y = 0b11010010

x0 = x ^ y
y0 = x0 ^ y # to find value of y0 by using value of x0
x1 = x0 ^ y0 # to fing value of x1 by using value of x0 and y0
print(f"1. Before swapping: x = {bin(x)}, y = {bin(y)}")
print(f'   After swapping: x = {bin(x1)}, y = {bin(y0)}')

# 2. toggle the 3rd and 5th bits of x
x = 0b10101100
mask = 0b00010100
print("2.", bin(x ^ mask))

# 3. check if two given numbers a = 29 and b = 15 are different
a = 29
b = 15
print(f"3. binary a = {bin(a)}")
print(f"   binary b = {bin(b)}")
print(f"   a = {a} and b = {b} are the same") if (bin(a) == bin(b)) else print(f"   a = {a} and b = {b} are different")

'''