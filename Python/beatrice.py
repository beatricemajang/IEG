string_with_quotes = "Hello, it's Beatrice."
another_with_quotes = 'He said \"You are amazing\" yesterday.'

print(string_with_quotes)
print(another_with_quotes)

""" 
strings

My name is Beatrice. I love AI Machine Learning
"""
multiline = """ 
My name is Beatrice. I love AI Machine Learning
"""
print(multiline)

age = 28
age_as_str = str(age)
print("My age is " + age_as_str)
print("Your age is ", age)
print(f"His age is {age}")

name = "Griffiths"
greeting = f"Hi, how are you, {name}?"
print(greeting)

name = "Leah"
final_greeting = "Hi, I'm fine {}, thank you."
leah_greeting = final_greeting.format(name)
print(leah_greeting)

friend_nama = "Yohanes"
final_greeting = "What do you eat for lunch, {name}?"
yohanes_greeting = final_greeting.format(name=friend_nama)
print(yohanes_greeting)

my_name = "Ezequiel"
your_name =  input("Your name: ")
print(f"Hello {your_name}. My name is {my_name}")

age = input("Your age: ")
age_num = int(age)
print(f"You have live for {age} years.")
print(f"You have live for {age * 12} months.")
print(f"You have live for {int(age) * 12} months.")
print(f"You have live for {age_num * 12} months.")

age = int(input("Your age: "))
months =  age * 12
print(f"You have live for {months} months.")

