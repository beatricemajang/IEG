num_1 = int(input("Enter first integer: "))
num_2 = int(input("Enter second integer: "))

def gcd(num_1,num_2):
  while num_2 != 0:
    num_1, num_2 = num_2, num_1 % num_2
  return num_1

statement = f"GCD({num_1},{num_2}) = {gcd(num_1,num_2)}"
print(statement)