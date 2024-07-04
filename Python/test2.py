# Write a simple Python function that takes a number(n) as a parameter
# display this:
#        1
#       1 1
#      1 2 1
#     1 3 3 1
#    1 4 6 4 1
#   1 5 10 10 5 1
#  1 6 15 20 15 6 1
# 1 7 21 35 35 21 7 1

def Pascal(n) :
    pascal = {}
    for line in range(0, n) :
        listinrow = []
        for i in range(0, line + 1) :
            listinrow.append(str(binomialCoeff(line,i)))
        pascal[line] = listinrow
    Pascal_Dict_to_List(pascal)

def Pascal_Dict_to_List(pascaldict):
    width = len(pascaldict) *3
    for i in range(0, len(pascaldict)):
        my_string = ' '.join(pascaldict[i])
        padding = " " * ((width - len(my_string)) // 2)
        print(f"{padding}{my_string}{padding}")

def binomialCoeff(n, k) :
    res = 1
    if (k > n - k) :
        k = n - k
    for i in range(0 , k) :
        res = res * (n - i)
        res = res // (i + 1)
    return res

n = int(input("Enter number of rows:"))
Pascal(n)

