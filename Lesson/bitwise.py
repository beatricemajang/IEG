# how to represent binary numbers in python
# you can use 0b followed by the binary number
# however, it is still an integer
# by adding 0b python starts resding it as one one
# instead of one hundred and eleven
ownerpermission = 0b111
print(ownerpermission)

# now owner can read, write an execute
# group can read and execute
# others can execute only
filepermission = 0b111101001

# in datascience /  machine learning when you were given
# categorical data you must convert them to numbers
# which machine can understand
# this itself called "feature engineering"
# gender representation: 01 for female or 10 for male
# race representation 100 for malay and 0100 for chinese

# this bit extraction can be use using bitwise and operator
mask = 0b000111000
print((filepermission & mask) >> 3)
# we manage to get group permission over the file

# in order to perform bit extraction, we use bitwise & operator (AND)
# we are interested in 4, 5, 6 bits only
# original data                111101001    &
# our mask (desired)           000111000
# bits extracted               000101000
# shift it to right 3 times    000000101    >> 3
print(bin((filepermission & mask) >> 3))

# The OR operator is used to set a specific bit to 1
# original data                111101001   | 
# our mask (desired)           000111000
# bits extracted               111111001
# please remember there is no way to set a specific bit to 0 using OR operator
# OR operator is also used in extracting region of interest in a image
print(bin(filepermission | mask))

# use NOT operator
# original data                01001010    ^
# our mask (desired)           00101100
# bits extracted               01100110
# XOR is used for encryption (SHA256 different from encrypt and decrypt process)
message = 0b01001010 # my content "J"
key = 0b00101100 # encryption key ","
encrypted_message = message ^ key
print(bin(encrypted_message))

decrypted_message = encrypted_message ^ key
print(bin(decrypted_message))

# 1s complement
givenNumber = 5
# 5                 0101
# 1s compliment     1010
print(~givenNumber) # 1s compliment
# 2s compliment     1s compliment + 1
print(~givenNumber + 1) # 2s compliment
print(-givenNumber) # - unary negative
print(+givenNumber) # + unary positive

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, 10
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
hexadecimalNumber =  0XF
print(hexadecimalNumber)
print(hex(hexadecimalNumber))

# 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
octalNumber = 0o10
print(octalNumber)
print(hex(octalNumber))