# pass-by-reference vs pass-by-value

# define a function that multiplies its input by 2

# Single values typically passed by value


def mult_by_2(x):
    x = x*2
    return x


y = 12
z = mult_by_2(y)
print(z)

myList = [1, 2, 3]

# Typically data structures passed into a function are passed by reference


def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2


print(myList)
mult2_list(myList)
print(myList)


def makeUpper(string):
    string = string.upper()
    return string


myString = "hello"

makeUpper(myString)
print(myString)

# Strings are pass by value

