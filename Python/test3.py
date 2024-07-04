num_1 = int(input(""))
num_2 = int(input(""))

for num in range(num_1, num_2 + 1):
    isPrime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        print(num, end=' ')