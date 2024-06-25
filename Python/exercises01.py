# given number is 97531
# I want you to reverse the number
# expected result is 13579

a0 = 97531
result =  a0 % 10
a1 = a0 // 10
print(result, a1)

result = (result * 10) + (a1 % 10)
a2 = a1 // 10
print(result, a2)

result = (result * 10) + (a2 % 10)
a3 = a2 // 10
print(result, a3)

result = (result * 10) + (a3 % 10)
a4 = a3 // 10
print(result, a4)

result = (result * 10) + (a4 % 10)
a5 = a4 // 10
print(result, a5)

# Akmal's Solution
a0 = 97531

result = (a0 % 10)* 10000
result = result + ((a0 // 10) % 10) * 1000
result = result + ((a0 // 100) % 10) * 100
result = result + ((a0 // 1000) % 10) * 10
result = result + ((a0 // 10000) % 10) * 1
print(result)

givenNumber = 97531
result = givenNumber % 10       # 1
givenNumber = givenNumber // 10            # 9753
givenNumber //= 10  # 9753
result = result * 10 + (givenNumber % 10)
givenNumber //= 10  #975
result = result * 10 + (givenNumber % 10)
givenNumber //= 10  #97
result = result * 10 + (givenNumber % 10)
givenNumber //= 10  #9
result = result * 10 + (givenNumber % 10)
givenNumber //= 10  #0
result = result * 10 + (givenNumber % 10)


print(0 % 4)