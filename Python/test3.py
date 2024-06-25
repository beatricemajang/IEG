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