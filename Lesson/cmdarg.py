# when we call python to execute our program, we can pass values to
# our program in  the command line which is also called command line arguments
# these arguments are separated by space
# all these arguments inside the list are string type
# remember the arguments for function is separated by comma

# sys.argv give us a list, which contain all the command line arguments
# passed to python
# in the list, you can see the item at position 0 is program name itself
import sys

# we are using dot (.) operator to access
# the variable which is inside the module sys
cmdarguments = sys.argv 
print(cmdarguments)

# find the total of all the arguments
# if we know the total number of arguments then we can hardcode it
# total = int(cmdarguments[1]) + int(cmdarguments[2])

# in this case, we have to use loops (since we do not know the total number of arguments)
total = 0
for number in cmdarguments[1:]:
    total = total + int(number)
print(total)