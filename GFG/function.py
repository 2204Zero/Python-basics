# Functions in Python - GeeksForGeeks

def func ():                             # declaring and defining function
    print("Hello World!")

func()                                   # calling the function

# the above function is a non parameterized function 

# Parameterized function 
def sum(a,b):
    return a + b

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

c = sum(a,b)

print(c)

# Default arguemnts of a function
def defaultArguments(x, y=190):            # 190 is assumed to be the default value
    print(x + y)

defaultArguments(10)

# Arguments as key 
def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')