# Aida
# any / all
# They are builtin functions
# They take boolean list as parameter
# [True, True, False, True, False, False]
# If any function take the above list as parameter it will return True
# Any true becomes True (any == or)
# If all function take the above list as parameter it will return False
# All true becomes True (all == and)
# check whether the given number is Prime number
givenNumber = 9
divisors = range(2, givenNumber)
# a list is given and we are going to create another list
if (len([mynumber for mynumber in divisors if (givenNumber % 2 == 0)]) == 0):
    print("Prime Number")
else:
    print("Not a Prime Number")

if any([givenNumber % mynumber == 0 for mynumber in divisors]):
    print("Not a Prime Number")
else:
    print("Prime Number")

# prime Number
# check whether the given number is prime or not
# check whether the input is prime or not
# generate first 10 prime numbers
# generate prime numbers between 10 to 100