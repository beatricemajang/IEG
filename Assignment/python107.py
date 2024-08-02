
## Problem 1:
'''
A pangram is a sentence using every letter of the alphabet at least once. It is case
insensitive, so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).
For this exercise, a sentence is a pangram if it contains each of the 26 letters in the 
English alphabet.

Example: The quick brown fox jumps over the lazy dog.
Your task is to figure out if a sentence is a pangram.
'''
'''
def is_pangram(string):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  if set(alphabet).issubset(set(string.lower())):
    return "The sentence is a pangram"
  else:
    return "The sentence is not a pangram"

sentence = "The quick brown fox jumps over the lazy dog."
sentence_1 = is_pangram(sentence)
print(sentence)
print(sentence_1)
'''



## Problem 2:
'''
An isogram (also known as a "non-pattern word") is a word or phrase without a repeating 
letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:
lumberjacks background downstream six-year-old
The word isograms, however, is not an isogram, because the s repeats.
Your task is to figure out if the user input is isogram
'''
'''
def is_isogram(string):
    string = string.lower().replace(" ", "").replace("-", "")
    if len(string) == len(set(string)):
        return f"The string of '{string}' is an isogram."
    else:
        return f"The string of '{string}' is not my an isogram."

string_1 = "lumberjacks background downstream six-year-old"
sentence = is_isogram(string_1)
print(sentence)
string_2 = str(input("Enter your own string: \n"))
sentence = is_isogram(string_2)
print(sentence)
'''



## Problem 3:
'''
Parse and evaluate simple math word problems returning the answer as an integer.
What is 5?    -> 5
What is 5 plus 13?    -> 13
What is 7 minus 5?    -> 2
What is 6 multiplied by 4?     -> 24
What is 25 divided by 5?       -> 5
What is 5 plus 13 plus 6?      -> 24
What is 3 plus 2 multiplied by 3?       -> 15
'''
'''
class Calculator:
    def __init__(self):
        pass

    def evaluate(self, problem: str) -> int:
        problem = problem.replace("What is", "").replace("by", "").replace("?", "")
        problem = problem.split()

        operations = {
            "plus": "+",
            "minus": "-",
            "multiplied": "*",
            "divided": "/"
        }

        result = int(problem[0])
        for i in range(1, len(problem), 2):
            op = operations[problem[i]]
            num = int(problem[i + 1])
            if op == "+":
                result += num
            elif op == "-":
                result -= num
            elif op == "*":
                result *= num
            elif op == "/":
                result //= num

        return result


calc = Calculator()
print("What is 5? ->", calc.evaluate("What is 5?"))
print("What is 5 plus 13? ->", calc.evaluate("What is 5 plus 13?"))
print("What is 7 minus 5? ->", calc.evaluate("What is 7 minus 5?"))
print("What is 6 multiplied by 4? ->", calc.evaluate("What is 6 multiplied by 4?"))
print("What is 25 divided by 5? ->", calc.evaluate("What is 25 divided by 5?"))
print("What is 5 plus 13 plus 6? ->", calc.evaluate("What is 5 plus 13 plus 6?"))
print("What is 3 plus 2 multiplied by 3? ->", calc.evaluate("What is 3 plus 2 multiplied by 3?"))
'''



## Problem 4:
'''
For this exercise, you need to know two things about them:
Each resistor has a resistance value. Resistors are small - so small in fact that if 
you printed the resistance value on them, it would be hard to read. To get around this 
problem, manufacturers print color-coded bands onto the resistors to denote their 
resistance values. Each band has a position and a numeric value.

The first 2 bands of a resistor have a simple encoding scheme: each color maps to a 
single number. For example, if they printed a brown band (value 1) followed by a green 
band (value 5), it would translate to the number 15.

In this exercise you are going to create a helpful program so that you don't have to 
remember the values of the bands. The program will take color names as input and output 
a two digit number, even if the input is more than two colors!
The band colors are encoded as follows:
1.   Black: 0
2.   Brown: 1
3.   Red: 2
4.   Orange: 3
5.   Yellow: 4
6.   Green: 5
7.   Blue: 6
8.   Violet: 7
9.   Grey: 8
10.  White: 9

From the example above:
brown-green should return 15
brown-green-violet should return 15 too, ignoring the third color
'''
'''
class Resistor:
    def __init__(self):
        self.color_map = {
            'black': 0,
            'brown': 1,
            'ed': 2,
            'orange': 3,
            'yellow': 4,
            'green': 5,
            'blue': 6,
            'violet': 7,
            'grey': 8,
            'white': 9
        }

    def get_resistance(self, colors):
        resistance = 0
        for i, color in enumerate(colors[:2]):
            resistance += self.color_map[color] * (10 ** (1 - i))
        return resistance

user = input("Enter the colours: \n").split()
resistance = Resistor()
print(resistance.get_resistance(user))
'''



## Problem 5:
'''
Your task is to Validate Credit Card Number
Given a number determine whether or not it is valid per the Luhn formula.
The Luhn algorithm is a simple checksum formula used to validate a variety of 
identification numbers, such as credit card numbers and Canadian Social Insurance Numbers.
The task is to check if a given string is valid

Valid credit card number
4539 3195 0343 6467

The first step of the Luhn algorithm is to double every second digit, 
starting from the right. We will be doubling
4_3_ 3_9_ 0_4_ 6_6_

If doubling the number results in a number greater than 9 then subtract 9 from the product. 
The results of our doubling:
8569 6195 0383 3437

Then sum all of the digits:
8+5+6+9+6+1+9+5+0+3+8+3+3+4+3+7 = 80

If the sum is evenly divisible by 10, then the number is valid. This number is valid!
'''
'''
def validate_credit_card_number(card_number):
    card_number = card_number.replace(" ", "")
    digits = [int(d) for d in card_number]
    digits = digits[::-1]

    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    total = sum(digits)
    return total % 10 == 0

card_number = "4539 3195 0343 6467"
if validate_credit_card_number(card_number):
    print(f"The credit card number of {card_number} is valid!")
else:
    print(f"The credit card number of {card_number} is not valid.")
'''



## Problem 6:
'''
Write a Python class that has two methods: getString and printString , The getString a
ccept a string from the user and printString prints the string in upper case.
'''
'''
class string:
    def __init__(self):
        self.input=""

    def getString(self):
        self.input=input("Enter a string:")
        return self.input

    def printString(self):
        return print(self.input.upper())

statement = string()
print(statement.getString())
statement.printString()
'''




## Problem 7:
'''
Write a Python class Employee with properties id, name, salary, and department and methods 
like _init_ calculateSalary, assignDepartment and _str_.

Sample Employee Data:

"E7876", "ADAMS", 50000, "ACCOUNTING"
"E7499", "JONES", 45000, "RESEARCH"
"E7900", "MARTIN", 50000, "SALES"
"E7698", "SMITH", 55000, "OPERATIONS"

Use 'assignDepartment' method to change the department of an employee.
Use '_str_' method to print the details of an employee.

Use 'calculateSalary' method takes two arguments: salary and hours_worked, which is the
number of hours worked by the employee. If the number of hours worked is more than 50, 
the method computes overtime and adds it to the salary.

Overtime is calculated as following formula: 
overtime = hours_worked - 50 Overtime amount = (overtime * (salary / 50))
'''
'''
class Employee:
    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department

    def calculateSalary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (self.salary / 50))
            return self.salary + overtime_amount
        else:
            return self.salary

    def assignDepartment(self, new_department):
        self.department = new_department

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Salary: {self.salary}, Department: {self.department}"

employees = [
    Employee("E7876", "ADAMS", 50000, "ACCOUNTING"),
    Employee("E7499", "JONES", 45000, "RESEARCH"),
    Employee("E7900", "MARTIN", 50000, "SALES"),
    Employee("E7698", "SMITH", 55000, "OPERATIONS")
]

for employee in employees:
    print(employee)

employees[0].assignDepartment("FINANCE")
print(employees[0])
print("Salary with overtime:", employees[0].calculateSalary(60))
'''



## Problem 8:
'''
Write a Python class Inventory with attributes like id, productName, availableQuantity 
and price. Add methods like addItem, updateItem, and checkItem_details.
Use a dictionary to store the item details, where the key is the id and the value is a 
dictionary containing the productName, availableQuantity and price.

Sample Data:

{
  "97410": {
    "name": "Television",
    "availableQuantity": 20,
    "price": 1455.99
  },
  "97411": {
    "name": "Radio",
    "availableQuantity": 32,
    "price": 654.25
  }
}
'''
'''
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, id, name, available_quantity, price):
        if id not in self.items:
            self.items[id] = {"name": name, "availableQuantity": available_quantity, "price": price}
        else:
            print("Item with this ID already exists.")

    def update_item(self, id, name=None, available_quantity=None, price=None):
        if id in self.items:
            if name:
                self.items[id]["name"] = name
            if available_quantity:
                self.items[id]["availableQuantity"] = available_quantity
            if price:
                self.items[id]["price"] = price
        else:
            print("Item with this ID does not exist.")

    def check_item_details(self, id):
        if id in self.items:
            return self.items[id]
        else:
            print("Item with this ID does not exist.")
            return None

barang = Inventory()
barang.add_item("97410", "Television", 20, 1455.99)
barang.add_item("97411", "Radio", 32, 654.25)
print(barang.check_item_details("97410"))
print(barang.check_item_details("97411"))
barang.update_item("97410", available_quantity=30)
print(barang.check_item_details("97410"))
'''



## Problem 9:
'''
Write a Python class BankAccount with attributes like accountNumber, openingBalance, 
currentBalance dateOfOpening and customerName. Add methods like deposit, withdraw, and 
checkBalance.
'''
'''
class BankAccount:
    def __init__(self, account_number, customer_name, opening_balance, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.current_balance = opening_balance

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Deposit Successful. Current Balance: {self.current_balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.current_balance:
            self.current_balance -= amount
            print(f"Withdrawal Successful. Current Balance: {self.current_balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Current Balance: {self.current_balance}")

leah = BankAccount("123456", "Beatrice", 500, "15 June 2021")
leah.deposit(10)
leah.withdraw(50)
leah.check_balance()
'''



## Problem 10:
'''
Write a Python class to check the validity of a string of parentheses,

'(', ')', '{', '}', '[' and '].

These brackets must be closed in the correct order, for example

"()" and "()[]{}" are valid
"[)", "({[)]" and "{{{" are invalid.
'''
'''
class CheckParentheses:
    def __init__(self, string):
        self.string = string

    def check(self):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in self.string:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif char in [')', '}', ']']:
                if not stack or mapping[char] != stack.pop():
                    return False
        return not stack

print('"()" is', CheckParentheses("()").check())
print('"()[]{}" is',CheckParentheses("()[]{}").check())
print('"[)" is',CheckParentheses("[)").check())
print('"({[)]" is',CheckParentheses("({[)]").check())
print('"{{{" is',CheckParentheses("{{{").check())
'''